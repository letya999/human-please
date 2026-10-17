# my_skills (delegate-skills subset)

This monorepo holds multiple independent agent skills. This document covers the
**delegate-skills** family only. Other top-level skill folders are separate
projects and are not part of this contract.

## Delegate skills

| Skill folder | Wrapper | CLI | Env override |
| --- | --- | --- | --- |
| `claude-code-delegate` | `scripts/delegate_claude.py` | `claude` (`claude -p`) | `CLAUDE_BIN` |
| `codex-delegate` | `scripts/delegate_codex.py` | `codex` (`codex exec`) | `CODEX_BIN` |
| `antigravity-delegate` | `scripts/delegate_antigravity.py` | `agy` (print mode) | `AGY_BIN` |
| `opencode-delegate` | `scripts/delegate_opencode.py` | `opencode` (`opencode run`) | `OPENCODE_BIN` |

Each skill runs its target CLI once as a headless subprocess (no shell), captures
stdout/stderr and a small result manifest under a temp directory, and prints a
JSON document that includes a `response` field when one can be extracted.

## Shared wrapper contract

All four wrappers accept at least:

```text
python scripts/delegate_<tool>.py --cwd <absolute-project-dir> --task <text> [--timeout 45m]
```

- `--cwd` must exist; missing directory exits with code `2`.
- `--timeout` accepts `90s`, `45m`, `2h`, or a bare number of seconds.
- `<TOOL>_BIN` overrides binary discovery (absolute path preferred).
- Binary not found exits with code `127`.
- Timeout exits with code `124`.
- Failed process start exits with code `126`.
- On success/failure of the child, the wrapper prints a JSON manifest (includes
  `response` when available) and returns the child exit code (or a dedicated
  parse/error code such as `65` when the child succeeded but produced no usable
  response).
- Auto-approve / full-access flags default to off. Do not pass them unless the
  caller explicitly wants edit/permission bypass.
- Results are unverified: inspect `git diff` and run tests after delegated edits.

## Tests

Each delegate skill has stdlib `unittest` coverage under `tests/`. Tests never
call the real CLI binaries and never use the network.

From the monorepo root:

```powershell
python -m unittest discover -s claude-code-delegate/tests -v
python -m unittest discover -s codex-delegate/tests -v
python -m unittest discover -s antigravity-delegate/tests -v
python -m unittest discover -s opencode-delegate/tests -v
```

Or per skill folder:

```powershell
cd claude-code-delegate
python -m unittest discover -s tests -v
```

Help smoke check for a wrapper:

```powershell
python claude-code-delegate/scripts/delegate_claude.py --help
```

## Scope

Do not treat other folders in this monorepo (for example `ai-repo-safety-skill`,
`confluence-gitlab-sync`, `jira-daily-pm-radar`) as part of the delegate contract.
They are independent skills with their own docs and tests.
