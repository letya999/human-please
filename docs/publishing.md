# Publication and skills.sh

## What is prepared

The publication target is [letya999/human-please](https://github.com/letya999/human-please). It contains a discoverable `human-please/SKILL.md`, MIT license, English and Russian user guides, synthetic evaluations, read-only CI and a package command. `dev` is the default development branch; protected `main` receives release PRs only from this repository's `dev`. Commands below use `OWNER/REPOSITORY` as a template for future maintainers; this project's value is `letya999/human-please`.

## Prepare a release

1. Review the exact tracked file list. This workspace also contains independent local projects; publish only the intended committed content.
2. Run the checks in CONTRIBUTING.md and inspect the built archive and checksum.
3. Review the changelog and synchronize the manifest version before an intentional release. The first public release is version 0.2.0.
4. Merge the reviewed feature into `dev`, then open a `dev` → `main` release PR. All three packaging/discovery checks and `main-from-dev` must pass. The source check uses base-branch `pull_request_target` metadata, no permissions, no checkout and no PR code execution. Main protection applies to administrators too; do not bypass it. After release, fast-forward `dev` to the main merge commit before starting another change.
5. Select or create a public repository, verify its default branch, and publish only after the owner explicitly requests those external actions.
6. Verify private vulnerability reporting and main branch protection on the selected host. Local files document these settings; the repository's GitHub configuration enforces them.

After the public source exists, verify discovery without installing:

```sh
npx skills@1.7.2 add OWNER/REPOSITORY --list
```

Users can then select the skill:

```sh
npx skills@1.7.2 add OWNER/REPOSITORY --skill human-please
```

Installation is an action affecting an agent's local configuration. Review the skill and choose the intended scope before installing. No install or publication command is part of the local package process.

## Listing and page configuration

The [official FAQ](https://skills.sh/docs/faq) says skills are listed through installation telemetry from the skills CLI. A public repository and a valid SKILL.md make the skill installable; they do not prove a listing exists or guarantee when it will appear.

[`skills.sh.json`](../skills.sh.json) follows the [official page customization documentation](https://skills.sh/docs/customize) and [schema](https://skills.sh/schemas/skills.sh.schema.json). It groups human-please under Understand. Commit it on the selected repository's default branch. It changes page presentation, not skill discovery or installation. According to that documentation, the service refreshes it after a telemetry-enabled installation and caching can delay updates.

Local verification and CI set `DISABLE_TELEMETRY=1`; they are not attempts to register or inflate a public listing. No npm package, registry credentials or custom publication API is required for the Git-hosted skill.

## Archives

`python tools/maintain.py` creates a deterministic ZIP-format `.skill` file containing the manifest, license and references. The SHA-256 sidecar allows a reviewer to compare downloaded bytes. A checksum does not prove that instructions are trustworthy; review the source and the release provenance.

The archive is a portable bundle, not a promise that every agent accepts `.skill` directly. Manual extraction into the host's documented skill directory remains available. Refer to the [Agent Skills specification](https://agentskills.io/specification) and [skills CLI documentation](https://github.com/vercel-labs/skills) for supported installation paths.
