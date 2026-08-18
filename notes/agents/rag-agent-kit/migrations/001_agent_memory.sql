-- RAG-агент с памятью — базовая схема.
--
-- ПОЧЕМУ так разделено: память агента (что говорил пользователь) и база знаний
-- (что знает система) — разные сущности с разным жизненным циклом. Корпус
-- переиндексируется, история чистится по срокам хранения, кэш протухает сам.
-- В одной таблице это всё превращается в неразбираемое месиво.
--
-- Перед применением: заменить TODO на реальную таблицу пользователей проекта.

-- =====================================================================
-- 1. БАЗА ЗНАНИЙ — то, по чему агент отвечает
-- =====================================================================

create table if not exists public.knowledge_documents (
  id            uuid primary key default gen_random_uuid(),
  slug          text not null unique,
  title         text not null,
  summary       text,
  body_md       text not null,
  kind          text not null default 'document',
  -- Уровень доступа: пользователь видит документ при user.access_level >= access_level.
  -- 0 = публичный. Нет платных уровней — оставь везде 0, логика не сломается.
  access_level  integer not null default 0,
  is_published  boolean not null default true,
  metadata      jsonb not null default '{}',
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now()
);

-- Выборка корпуса всегда идёт по published + access_level.
create index if not exists idx_knowledge_documents_published
  on public.knowledge_documents (is_published, access_level);

comment on table public.knowledge_documents is
  'Корпус знаний агента. Одна строка = один документ.';
comment on column public.knowledge_documents.access_level is
  'Минимальный уровень доступа пользователя. 0 = доступно всем.';
comment on column public.knowledge_documents.body_md is
  'Полный текст в markdown. Целиком в промпт НЕ уходит — только фрагмент вокруг совпадения.';

-- =====================================================================
-- 2. ТРЕДЫ — длинная память
-- =====================================================================

create table if not exists public.agent_conversations (
  id              uuid primary key default gen_random_uuid(),
  -- TODO: заменить на references public.<таблица_пользователей>(id) on delete cascade
  user_id         uuid not null,
  title           text,                    -- генерируется фоном после первого ответа
  archived_at     timestamptz,             -- мягкое удаление
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now(),
  last_message_at timestamptz not null default now()
);

-- Основной запрос: последние треды пользователя.
create index if not exists idx_agent_conversations_user
  on public.agent_conversations (user_id, last_message_at desc);

comment on table public.agent_conversations is 'Разговоры пользователя с агентом.';

-- =====================================================================
-- 3. СООБЩЕНИЯ — короткая память
-- =====================================================================

create table if not exists public.agent_messages (
  id              uuid primary key default gen_random_uuid(),
  conversation_id uuid not null
                  references public.agent_conversations(id) on delete cascade,
  role            text not null check (role in ('user', 'assistant')),
  content         text not null,
  sources         jsonb,                   -- [{kind, slug, title}] — только у assistant
  tokens_used     integer,                 -- input + output; 0 у ответов из кэша
  created_at      timestamptz not null default now()
);

-- Чтение истории треда по порядку.
create index if not exists idx_agent_messages_conversation
  on public.agent_messages (conversation_id, created_at);

comment on column public.agent_messages.sources is
  'Только {kind, slug, title}. Внутренние score/snippet сюда не пишутся.';

-- =====================================================================
-- 4. КЭШ ОТВЕТОВ — память о вопросах
-- =====================================================================

create table if not exists public.agent_response_cache (
  -- Формат: <sha256 нормализованного вопроса>:<access_level>.
  -- Уровень доступа в ключе ОБЯЗАТЕЛЕН: без него пользователь с низким уровнем
  -- получит из кэша ответ, сгенерированный по недоступному ему контексту.
  query_hash    text primary key,
  answer        text not null,
  sources       jsonb,
  hit_count     integer not null default 0,
  tokens_saved  integer not null default 0,
  created_at    timestamptz not null default now(),
  last_hit_at   timestamptz,
  expires_at    timestamptz not null default (now() + interval '30 days')
);

create index if not exists idx_agent_cache_expires
  on public.agent_response_cache (expires_at);
create index if not exists idx_agent_cache_hits
  on public.agent_response_cache (hit_count desc);

comment on table public.agent_response_cache is
  'Кэш ответов на первое сообщение треда. При попадании модель не вызывается.';
comment on column public.agent_response_cache.tokens_saved is
  'Расход исходного вызова — база для подсчёта экономии.';

-- =====================================================================
-- 5. RLS — защита в глубину
-- =====================================================================
-- Приложение ходит через service_role и проверяет доступ в коде.
-- RLS всё равно включаем: если кто-то однажды создаст публичный эндпоинт
-- с анонимным ключом, политики не дадут утечь ни истории, ни корпусу.

alter table public.knowledge_documents   enable row level security;
alter table public.agent_conversations   enable row level security;
alter table public.agent_messages        enable row level security;
alter table public.agent_response_cache  enable row level security;

create policy "service_role_all_knowledge_documents"
  on public.knowledge_documents for all to service_role using (true) with check (true);
create policy "deny_anon_knowledge_documents"
  on public.knowledge_documents for all to anon using (false);
create policy "deny_authenticated_knowledge_documents"
  on public.knowledge_documents for all to authenticated using (false);

create policy "service_role_all_agent_conversations"
  on public.agent_conversations for all to service_role using (true) with check (true);
create policy "deny_anon_agent_conversations"
  on public.agent_conversations for all to anon using (false);
create policy "deny_authenticated_agent_conversations"
  on public.agent_conversations for all to authenticated using (false);

create policy "service_role_all_agent_messages"
  on public.agent_messages for all to service_role using (true) with check (true);
create policy "deny_anon_agent_messages"
  on public.agent_messages for all to anon using (false);
create policy "deny_authenticated_agent_messages"
  on public.agent_messages for all to authenticated using (false);

create policy "service_role_all_agent_response_cache"
  on public.agent_response_cache for all to service_role using (true) with check (true);
create policy "deny_anon_agent_response_cache"
  on public.agent_response_cache for all to anon using (false);
create policy "deny_authenticated_agent_response_cache"
  on public.agent_response_cache for all to authenticated using (false);
