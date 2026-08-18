-- ЭТАП 2 — векторный поиск. Применять ТОЛЬКО когда сработал критерий перехода
-- (MANUAL.md, раздел «Когда переходить на векторы»). До этого поиск по ключевым
-- словам из Этапа 1 даёт ту же точность без пайплайна эмбеддингов.
--
-- Размерность 1024 = Voyage AI voyage-3. Меняешь модель эмбеддингов — меняешь
-- размерность здесь И пересчитываешь всю таблицу: смешивать в одной колонке
-- векторы от разных моделей нельзя, близость между ними не значит ничего.

-- ВНИМАНИЕ, Supabase: расширение живёт в схеме extensions, а не в public.
-- Тип тогда пишется как extensions.vector(1024), а оператор класса — как
-- extensions.vector_cosine_ops. На чистом Postgres — без префикса, как ниже.
-- Скопировал файл, получил «type vector does not exist» — это оно.
create extension if not exists vector;

-- =====================================================================
-- Чанки: документ, порезанный на куски, каждый со своим вектором
-- =====================================================================

create table if not exists public.knowledge_chunks (
  id           uuid primary key default gen_random_uuid(),
  document_id  uuid not null
               references public.knowledge_documents(id) on delete cascade,
  chunk_index  integer not null,
  content      text not null,
  -- Voyage voyage-3, input_type='document' при индексации.
  embedding    vector(1024),
  metadata     jsonb not null default '{}',
  created_at   timestamptz not null default now(),
  -- Переиндексация делается через upsert по этой паре, а не delete+insert:
  -- иначе при сбое посреди процесса документ останется без чанков.
  unique (document_id, chunk_index)
);

create index if not exists idx_knowledge_chunks_document
  on public.knowledge_chunks (document_id);

-- ВАЖНО: ivfflat строится ПОСЛЕ заливки данных. Индекс, построенный по пустой
-- таблице, кластеризован по пустоте и работает хуже полного перебора.
-- lists = 100 — разумный старт до ~1 млн чанков.
create index if not exists idx_knowledge_chunks_embedding
  on public.knowledge_chunks
  using ivfflat (embedding vector_cosine_ops)
  with (lists = 100);

comment on table public.knowledge_chunks is
  'Чанки документов с эмбеддингами. 500-1500 символов, перекрытие 10-15%.';
comment on column public.knowledge_chunks.embedding is
  'Voyage voyage-3, 1024 измерения. Индексация: input_type=document. Поиск: input_type=query.';

-- =====================================================================
-- Семантический поиск с фильтром доступа
-- =====================================================================
-- Фильтр по access_level применяется ВНУТРИ функции, до limit.
-- Отфильтруешь снаружи после limit — недоступные чанки вытеснят доступные
-- из выдачи, и пользователь получит «ничего не найдено» при полной базе.

create or replace function match_knowledge_chunks(
  query_embedding  vector(1024),
  user_access_level integer default 0,
  match_threshold  float default 0.7,
  match_count      int default 8
)
returns table (
  id          uuid,
  document_id uuid,
  slug        text,
  title       text,
  content     text,
  similarity  float
)
language sql stable
as $$
  select
    c.id,
    c.document_id,
    d.slug,
    d.title,
    c.content,
    1 - (c.embedding <=> query_embedding) as similarity
  from public.knowledge_chunks c
  join public.knowledge_documents d on d.id = c.document_id
  where d.is_published
    and d.access_level <= user_access_level
    and 1 - (c.embedding <=> query_embedding) > match_threshold
  order by c.embedding <=> query_embedding
  limit match_count;
$$;

comment on function match_knowledge_chunks is
  'Поиск по косинусной близости с фильтром доступа. На вход — эмбеддинг запроса
   (input_type=query). Порог 0.7 — стартовый, подбирается под свой корпус.';

grant execute on function match_knowledge_chunks to service_role;

-- =====================================================================
-- RLS
-- =====================================================================

alter table public.knowledge_chunks enable row level security;

create policy "service_role_all_knowledge_chunks"
  on public.knowledge_chunks for all to service_role using (true) with check (true);
create policy "deny_anon_knowledge_chunks"
  on public.knowledge_chunks for all to anon using (false);
create policy "deny_authenticated_knowledge_chunks"
  on public.knowledge_chunks for all to authenticated using (false);
