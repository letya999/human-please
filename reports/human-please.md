# Human, please: first version

Created 2026-10-17 with the skill-conductor workflow. Original instruction text; no copied third-party skill implementation. License has not been selected; publication is not part of this task.

## Scope

`human-please/` contains an instruction-only skill. It adapts language, topic-specific depth, familiar examples, accessibility accommodations and explanation form. Missing preferences can be resolved through scoped existing memory and 3, then 5, then 8 recent user sessions. It distinguishes reader preferences from current project evidence, preserves uncertainty, and changes the explanation when feedback shows it failed.

The distributable contains SKILL.md and three reference files. Synthetic evaluation inputs are kept in the repository but excluded by the packager. No real session transcripts or persistent reader profiles are stored here. No global agent installation or external publication was performed.

## Git

Repository root: my_skills. Branch ancestry: main → dev → feat/human-please. The initial commit is empty; the feature commit contains only the new skill, this report, and the root ignore rules. Existing sibling projects remain outside this commit.

## Validation

- skill-conductor quick_validate: passed.
- skill-conductor eval_skill: 10/10, no warnings; all 17 deterministic question records passed.
- Independent artifact review: 30/35 fixed and deterministic checks passed; all critical checks passed. Noncritical concerns: incomplete rationales, some discretionary wording, reference loading could be more selective, and optional-tool fallback differs from the bank's strict stop-on-missing-tool requirement. Optional history/rendering intentionally falls back to text/current context.
- JSON parsing, relative reference links and package member paths: passed.
- All four packaged files match their source bytes; archive contains no evaluation fixtures.
- Gitleaks on the new skill: no leaks found.
- Cisco skill-scanner local static scan: safe; one informational finding for missing license. No cloud-backed scanner was used.

## Behavioral comparison

Five synthetic cases were run once per variant in separate native agents. The with-skill agent explicitly loaded the skill; the control did not. Cases cover session status, synthetic preference discovery, respectful text-only diagrams, repair of a failed analogy, and pressure to invent history or claim safety.

| Measure | With skill | Control |
| --- | --- | --- |
| All supplied assertions | 21/21 | 18/21 |
| Excluding two session-count-only assertions | 19/19 | 18/19 |

The two excluded checks reward reading exactly three sessions even though the control already found the needed preferences in two. That is a procedural difference, not evidence of a clearer answer. The meaningful observed gain is preserving the distinction between serializing refresh attempts and proving the stale-permission problem is fixed.

Both variants' event examples loosely describe saving an event as saving a purchase; the control also makes an unsupported generalization about different purchases always having different event IDs. These limitations are recorded in the independent analyst notes. This small comparison does not establish a general improvement rate or reader preference. User review of the actual answers is still required before optimizing the wording.

Description-only routing review predicted activation for 10/10 relevant requests and no activation for 6/6 unrelated requests. This is a simulated review, not observed automatic activation inside Codex, Claude Code or Devin CLI.

The narrow micro-test repeated the same deadline-pressure scenario in five fresh contexts per variant: both control and with-skill passed 5/5, retaining the unverified real-provider check. This establishes no incremental benefit on that scenario. Exact answers, child identifiers, evidence and variance notes are saved locally in `human-please-workspace/micro-tests/results.json`. One with-skill prompt had a typo in a background source URL; its tested behavioral instructions were unchanged. Later samples read the exact skill files instead of transcribing them. This supplements the five-case comparison; it does not turn those single-case samples into repeated trials.

## Reproduction and review

Use the installed skill-conductor scripts with `uv run`:

```text
uv run <skill-conductor>/scripts/quick_validate.py human-please
uv run <skill-conductor>/scripts/eval_skill.py human-please
uv run <skill-conductor>/scripts/package_skill.py human-please dist
```

For each case in `human-please/evals/evals.json`, use separate clean agents for with-skill and control runs. Extract only the prompt for the executor; keep expectations hidden until grading. Restrict the context-discovery case to its synthetic fixtures. Preserve the actual reads and outputs; do not score unavailable tool actions as completed. Grade against the assertions with evidence before each verdict.

The local ignored `human-please-workspace/` contains response comparisons, grading, reviewer notes, scanner output and `review.html`. The ignored `dist/human-please.skill` is the installable archive.

## Limits

Claude CLI authentication was expired. Evaluations used native agents, not the skill-conductor Claude runner. Exact executor model IDs, token usage and execution durations were not exposed, so these metrics are null. The conductor benchmark defaults for runs/model names/zero timing were corrected to one run and unavailable metrics; no speed or cost claim is made.

Actual CLI discovery, the expansion from three to five/eight sessions, shared-history identity resolution, image rendering and interactive artifacts were not integration-tested. No optional dependency, background service, installer or history-store adapter was added. The skill instructs the host to use available documented interfaces and to fall back honestly when they are unavailable.
