---
type: note
created: 2026-07-05
source: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
tags:
  - agents
  - ai
  - claude-code
  - dev-tools
  - security
  - skills
moc: "[[AI]]"
---
# Anthropic Cybersecurity Skills

Источник: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)  
Связи: [[Claude Code]], [[Безопасность skills]], [[Claude Code Security Guidance]], [[Awesome Harness Engineering]], [[AI Engineering from Scratch]]

## Что это

**Anthropic Cybersecurity Skills** — большая open-source библиотека structured skills для AI-агентов в кибербезопасности.

По README проекта: **817 cybersecurity skills**, **29 security domains**, формат [agentskills.io](https://agentskills.io), совместимость с Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI и другими агентскими платформами.

## Что внутри

Skills покрывают практические security-сценарии: DFIR, malware analysis, cloud security, AppSec, threat hunting, IAM/Active Directory, network security, compliance, supply chain security, deception, hardware/firmware и другие домены.

Каждый skill устроен как мини-playbook:

- `SKILL.md` с YAML frontmatter и Markdown-инструкциями;
- `references/` со стандартами и workflow;
- `scripts/` с helper-скриптами;
- `assets/` с шаблонами/checklists/report templates.

## Framework mapping

Проект маппит skills на несколько security-frameworks:

- MITRE ATT&CK;
- NIST CSF 2.0;
- MITRE ATLAS;
- MITRE D3FEND;
- NIST AI RMF;
- MITRE Fight Fraud Framework / F3.

Ценность не только в списке skills, а в том, что агент получает **структурированный security-контекст + связи со стандартами**, а не просто общие советы.

## Зачем Данилу

- **Для Claude Code / Codex:** референс, как должны выглядеть качественные domain-specific skills: структура, prerequisites, workflow, verification, references.
- **Для агентства:** можно использовать как пример библиотеки playbooks для узких доменов: amoCRM, аналитика, интеграции, QA, support, data extraction.
- **Для безопасности AI-разработки:** полезно как чеклист-подход: skill должен не только выполнять задачу, но и проверять результат.
- **Для личной базы:** хороший пример масштабной skill-library, которую можно не ставить целиком, а разбирать как архитектурный паттерн.

## Ограничения и риски

- Кибербезопасность — dual-use зона. Skills могут помогать defensive work, но часть техник потенциально применима злоумышленниками.
- Нельзя бездумно подключать всю библиотеку к агенту с доступом к production/клиентским данным.
- Нужны allowlist, sandbox, audit logs и явные границы: что агент может запускать, читать и отправлять наружу.
- Качество отдельных skills надо проверять выборочно: большой размер библиотеки не гарантирует одинаковую глубину каждого playbook.
- Название не означает официальную связь с Anthropic; README прямо указывает, что проект не affiliated with Anthropic PBC.

## Практическое применение

Лучший сценарий — **использовать как эталон структуры skills**, а не сразу устанавливать всё:

1. выбрать 3–5 defensive skills;
2. посмотреть формат `SKILL.md`, workflow, verification, references;
3. адаптировать структуру под внутренние агентские playbooks;
4. отдельно протестировать security-boundaries: sandbox, permissions, logging;
5. только после этого думать о частичном подключении к Claude Code/Codex.

## Мой вывод

Сильный ресурс как **референс mature skill-library для AI-агентов**. Главная польза для Данила — не «поставить 817 skills», а понять, как проектировать доменные skills: с prerequisites, workflow, verification, references и mapping на стандарты. Для рабочей среды — только выборочно и с жёсткими ограничениями безопасности.
