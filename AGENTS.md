# Repository instructions

This repository currently tracks human-please and its maintenance files. Other sibling skill folders can be independent local projects. Follow their own instructions and licenses when explicitly working on them.

## Human-please scope

- Read README.md, CONTRIBUTING.md and docs/testing.md before changing the skill or release tooling.
- Keep SKILL.md a short map; put method, context and visualization details in its existing references.
- Write instructions and contributor documentation in English. Multilingual user utterances belong in synthetic evaluation fixtures.
- Preserve topic-specific knowledge, current language preferences, known accessibility needs, scoped 3/5/8 history, and evidence limits.
- Keep events/messages distinct from business objects. Never turn reported or isolated-test success into verified integration success.
- Use skill-conductor for behavior changes: snapshot the prior version, freeze the evaluation split before results, keep held-out evidence out of editing, and compare fresh contexts. Report explicit activation separately from automatic CLI discovery.
- Keep runtime instruction-only. Maintenance code uses Python 3.12+ standard library. Add a dependency only for a demonstrated need.
- Run `python -m json.tool skills.sh.json`, `python tools/maintain.py`, then `python -m unittest discover -s tests -v` before delivery.
- Have new or changed tests reviewed by an independent test-critic before execution. A static review does not prove tests pass.
- Package only the manifest, skill license and references. Keep real transcripts, reader profiles, credentials, generated runs and sibling projects out of releases.
- Stage exact paths; do not use broad staging in this workspace. External publication, pushes and sending data require an actual user instruction for that action.
- Keep CI read-only with pinned action revisions. Treat publication instructions and skills.sh page configuration as preparation, not a claim of being listed.

The original delegate-specific rules follow. They apply only to the folders they explicitly name.

---

# AGENTS.md — delegate-skills subset

Machine-facing conventions for the five headless CLI delegate skills in this
monorepo. Other top-level skill folders are out of scope for this file.

## Skills in scope

| Folder | Script | Binary | Env |
| --- | --- | --- | --- |
| `claude-code-delegate` | `scripts/delegate_claude.py` | `claude` | `CLAUDE_BIN` |
| `codex-delegate` | `scripts/delegate_codex.py` | `codex` | `CODEX_BIN` |
| `antigravity-delegate` | `scripts/delegate_antigravity.py` | `agy` | `AGY_BIN` |
| `opencode-delegate` | `scripts/delegate_opencode.py` | `opencode` | `OPENCODE_BIN` |
| `pi-delegate` | `scripts/delegate_pi.py` | `pi` / `omp` | `PI_BIN` / `OMP_BIN` |

## Wrapper contract

- Invoke via `python <script> --cwd <abs-dir> --task <text> [--timeout ...]`.
- No shell: wrappers use `subprocess.run([...], shell=False)` only.
- Honor `<TOOL>_BIN` before PATH / well-known install locations.
- Print a JSON manifest; surface the human-facing result under `response`.
- Exit codes: `2` bad cwd, `127` binary not found, `124` timeout, `126` start
  failure, `65` missing/unusable response when the child claimed success,
  otherwise the child process exit code.
- Temp output dirs use prefixes such as `claude-code-delegate-` (gitignored via
  `*-delegate-*/` at repo root when created in-tree).

## Safety posture

- Default: no auto-approve, no full-access, no permission bypass flags.
- Never read or print credentials: API keys, tokens, `.env*`, `auth.json`,
  private keys, browser profiles, or vendor credential stores.
- Never install packages, run installers, commit, or push unless the user
  explicitly requests that exact action.
- Delegated agent output is unverified. Always check with `git diff` and tests
  before treating work as done.
- Do not recurse: a delegated agent must not re-delegate to the same CLI in a
  loop unless the user asks for multi-level orchestration.

## Scope boundary

- Allowed for delegate work: the four folders above and the root hygiene files
  (`.gitignore`, `README.md`, `AGENTS.md`) that document this subset.
- Independent and untouched by this contract: `ai-repo-safety-skill`,
  `confluence-gitlab-sync`, `grill-my-resume-as-manager`, `jira-daily-pm-radar`,
  `no_complex_book`, `skills_resume_check`, `spec-review`, `spec-write`,
  `twinby-context`, and any other non-delegate folder.
- No `README.md` inside a skill folder (skill packaging rule). Skill docs live
  in `SKILL.md` and `references/` only.
