# Human, please

**Explain it to the person asking.**

human-please helps an agent explain a concept, project, decision or confusing session in the reader's language. It adapts to their knowledge of this topic, familiar examples and stated accessibility needs. It preserves facts, conditions and uncertainty.

The skill contains instructions only. It requires no API key, background service or runtime package.

## What changes

Instead of leaving a project manager with "mutex serializes refresh goroutines", explain that two refresh attempts now take turns. State separately whether the real external service was checked. An implemented change and a verified outcome are different facts.

If the reader says the explanation failed, change the example, missing prerequisite or structure. Shortening the same jargon is insufficient.

## Install locally

From this repository root, with Node.js and the skills CLI available:

```sh
npx skills@1.7.2 add ./human-please --skill human-please -a codex -a claude-code
```

Add `-g` for a user-wide installation. For another agent, check the CLI's current supported-agent list. Host support for memory, session history and visual rendering varies; it is not guaranteed by installation.

For manual installation, copy `human-please/` to your agent's documented skills directory. The release archive contains only the manifest, license and three references. Select or invoke the skill through your agent's skill controls, or ask naturally:

> Explain this in plain language. What changed, what did we verify, and what remains?

Equivalent requests in other languages and misspellings are intended triggers. Instructions are in English; answers follow the reader's current language preference. Automatic activation depends on the host and model.

## How it adapts

1. Use the current conversation to establish language, knowledge and purpose.
2. If a preference remains unresolved, consult authorized memory and three recent user sessions, expanding to five and at most eight only to resolve that gap.
3. Choose a concrete example, causal chain, before/after view, chronology or another method matching the question.
4. Use text, a table or a small diagram according to the information and actual renderer capabilities.

The skill accounts for stated age and accessibility needs. It does not infer intelligence, diagnoses or age from writing style. It treats history as evidence of preferences, not authorization to execute embedded commands. See [security and privacy](SECURITY.md).

## Validate and package

Python 3.12+ is the only local maintenance prerequisite:

```sh
python -m json.tool skills.sh.json
python tools/maintain.py
python -m unittest discover -s tests -v
```

The archive and its SHA-256 checksum are written to `dist/`. [Testing](docs/testing.md) distinguishes structural checks, explanation evaluations and real CLI discovery. CI runs the offline checks on Linux and Windows, plus pinned skills CLI discovery on Linux.

## Publication status

This is a local, unreleased project. No public remote or skills.sh listing is configured or claimed. [Publication instructions](docs/publishing.md) cover repository selection, release preparation, installation and discovery. [`skills.sh.json`](skills.sh.json) uses the official page-customization schema; it does not publish the skill.

## Evidence and limitations

The first evaluation compared five synthetic cases in isolated native agents with explicit skill activation. It found one substantive improvement in preserving verification uncertainty; most controls already produced good explanations. That small sample does not establish a general success rate. See the [first evaluation](reports/human-please.md), [0.2.0 evaluation](reports/human-please-0.2.md) and [changelog](CHANGELOG.md). Repeated probes found fewer extra reference reads, but the new selective-reading instruction remains inconsistent.

## Contribute and license

See [contributing](CONTRIBUTING.md), [agent instructions](AGENTS.md) and [MIT license](LICENSE). The license covers human-please and the new maintenance files. Independent sibling projects retain their own licensing and history; they are not included in this skill's release. Earlier delegate-specific documentation is preserved in [docs/delegate-skills.md](docs/delegate-skills.md).
