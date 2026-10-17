# Human-please release 0.2.0

Adaptive plain-language explanations in the reader's language.

## Highlights

- Explain concepts, project status, confusing sessions and decisions.
- Adapt to the current reader, topic knowledge and stated preferences.
- Use authorized memory only when context is missing, with a bounded 3/5/8-session search.
- Preserve facts, business objects and verification uncertainty.
- Choose useful analogies, examples, tables and diagrams supported by the host.
- English runtime instructions; English and Russian project documentation.
- Original generated icon and banner, with documented prompts and provenance.

## Install

```sh
npx skills@1.7.2 add letya999/human-please --skill human-please
```

The `.skill` file is a ZIP containing only SKILL.md, LICENSE and three references. Compare its SHA-256 with the supplied checksum; unpack into your host's skill directory if direct archive installation is unsupported.

## Evidence and limits

Five packaging regression tests pass locally. The prior behavioral comparison improved from 14/15 to 15/15 assertions in five synthetic cases; its improvement concerned unnecessary reference reads. This is not a general explanation-quality score. Automatic activation, live memory integration and visualization vary by host. See the repository's evaluation report and Actions results for scope and evidence.

---

**По-человечески, пожалуйста** — объяснения на твоём языке, с учётом твоих знаний и без снисходительности. Установка приведена выше; русский README доступен в репозитории. Архив содержит только инструкции и справочники. Автосрабатывание и доступ к памяти зависят от клиента.
