# Testing

## Offline gates

`python -m json.tool skills.sh.json` checks configuration syntax. The official skills CLI checks manifest discovery; its listing step is separate because obtaining that CLI can require network access. The page configuration follows the official skills.sh schema and is reviewed against it before publication.

`python -m unittest discover -s tests -v` exercises the actual packager and released archive, including an exact runtime allowlist, unsafe source links, deterministic output and current archive contents. Test fixtures are temporary synthetic copies. These tests prove packaging behavior, not the quality of explanations or a remote agent integration.

`python tools/maintain.py` creates an allowlisted archive and writes its SHA-256 checksum. Run it before the archive tests. It does not install, publish, read user history or call an external service.

The GitHub Actions workflow runs offline checks on Linux and Windows. A separate Linux step asks a pinned skills CLI to list the local skill with telemetry disabled. That step checks discovery only; it does not prove automatic activation for a user request.

## Branch policy verification

The required `main-from-dev` check accepts only `dev` from this repository; both the branch name and repository identity must match. It runs from the trusted default-branch workflow without checking out PR code. On 2026-10-17, [release PR #5](https://github.com/letya999/human-please/pull/5) passed this check, while [non-dev probe PR #6](https://github.com/letya999/human-please/pull/6) failed with the intended source-policy error and was closed without merging. This exercises real GitHub events for the accepted and rejected branch paths; no fork was created to test the separate repository-identity condition. GitHub protection requires this check, the three packaging/discovery checks and a PR, with administrator enforcement and no force push or deletion.

## Explanation evaluations

Use skill-conductor for changes to instructions:

1. Snapshot the previous manifest and references outside the distributable.
2. Write concrete synthetic cases and freeze a train/held-out split before inspecting results.
3. Run old and candidate variants in separate fresh contexts. Give executors the prompt, not assertions or previous outputs.
4. Keep train evidence available for edits and held-out evidence for a separate regression gate. Record actual reads and operations; unavailable timing/token data remains null.
5. Grade meaning, reader fit and preserved uncertainty with cited evidence. Read the responses rather than trusting a count alone.
6. Reject a reproducible held-out regression; claim improvement only when the observed evidence supports it.
7. Show the answer comparison before another subjective wording pass.

Synthetic reader utterances remain multilingual intentionally. Instruction language and response language are separate requirements.

The exported `human-please/evals/advanced.json` and its fictional fixtures reproduce the second comparison's scenarios. They are public regression cases after export; choose new unseen cases for a future hidden holdout. Merely rewriting fixture paths for export does not count as rerunning the evaluations.

The original evaluation contains two over-specific session-count assertions. Treat their results as procedural checks, not proof of a clearer answer. New cases should verify that the needed preference was resolved without unauthorized or unnecessary reads.

## Real host checks

Automatic activation, shared-history identity, real session-store access, Mermaid rendering and interactive visuals require the actual target host. Record the host/version, available tools, exact request, observed skill activation and outcome. A simulated routing review or explicit file read does not establish these results. Use fictional context for repeatable checks; do not commit actual chats.
