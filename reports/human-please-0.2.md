# Human, please 0.2.0 preparation

Date: 2026-10-17. Status: local unreleased candidate; no public remote, push, release or skills.sh listing has been created.

## Changes

- English instructions and trigger description; multilingual user utterances remain in test data.
- MIT license in the repository and distributable; independent sibling projects retain their terms.
- Conditional reference loading and an explicit preference-resolution rule with a bounded 3/5/8 search.
- Source fidelity: messages/events remain distinct from business objects, and reported or isolated-test success remains distinct from integration verification.
- README, agent rules, contribution/privacy guidance, changelog, GitHub templates and pinned read-only CI.
- Official skills.sh page configuration and publication guidance; no custom publication API or registry credentials.
- Small standard-library packager with an explicit five-file allowlist, SHA-256, fixed ZIP metadata, source/output link rejection and preservation of an existing release when an input is missing.

Earlier delegate-specific documentation was preserved in docs/delegate-skills.md. The existing scoped delegate rules remain in AGENTS.md.

## Skill-conductor comparison

The previous manifest and references were snapshotted before editing. Five new synthetic scenarios were split before results into three train and two held-out cases. Old and candidate variants ran in ten separate fresh native contexts. An independent reviewer graded held-out evidence; it was not used to form instruction edits.

| Scope | Old | Candidate |
| --- | --- | --- |
| Train assertions | 8/9 | 9/9 |
| Held-out assertions | 6/6 | 6/6 |
| All assertions | 14/15 | 15/15 |

There was one improved assertion, fourteen stable assertions and no observed regressions. The improvement concerns avoiding optional reference reads when the current session supplies sufficient context. No general readability or accuracy improvement rate is established.

A supplemental narrow probe repeated that scenario five times per variant, counting the original isolated run as the first sample and adding four fresh runs. Old reference counts were [3, 3, 3, 3, 3]; candidate counts were [0, 0, 1, 1, 1]. All ten answers preserved the supplied facts. Thus the candidate reduces unnecessary reading in this sample, but obeys the zero-optional-read criterion only 2/5 times. No further wording changes were made after this evidence.

Exact snapshots, reads, responses, grades, transition data and the answer viewer are in the ignored human-please-workspace/iteration-2 directory. Token, timing and exact model metadata unavailable from the native interface remain null. The five new scenarios and fictional history were exported to human-please/evals/advanced.json and fixtures/advanced with portable paths only. That export was not a new evaluation run, and those now-visible cases are no longer hidden holdouts for future editing.

## Local evidence

- skill-conductor quick_validate passed; eval_skill scored 10/10 with no warnings.
- Official skills CLI 1.7.2 discovered exactly human-please from the local skill directory with telemetry disabled. It was invoked using the existing Bun runner because npm was unavailable. This verifies local discovery, not automatic activation in a chat.
- Five packaging regression tests passed on Windows, including both source/output symlink cases without skips.
- Each new regression test received independent static test-critic review before execution. Missing-license, missing-checksum, source-mtime, symlink and missing-input failures were observed before the corresponding fixes.
- The actual archive contains current bytes for SKILL.md, LICENSE and the three references. Evaluation inputs, repository documentation and local context are excluded.

The GitHub workflow has not run on a hosted repository. Its Linux and Windows jobs, npm-based discovery and artifact upload remain configured rather than observed. Automatic activation, real memory-store access, shared-user identity and interactive rendering remain host-specific checks. Claude CLI authentication was expired; no login was attempted.
