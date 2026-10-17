# Contributing

Start with a concrete explanation that failed its reader. Include the reader's stated background, their question, the answer they received, and what they still could not understand. Use synthetic examples or remove private details.

## Local checks

Python 3.12 or newer is sufficient. There are no runtime or test dependencies to install.

```sh
python -m json.tool skills.sh.json
python tools/maintain.py
python -m unittest discover -s tests -v
```

The package command produces a reproducible `dist/human-please.skill` archive and SHA-256 checksum. It includes only the manifest, license and explanation references.

## Changes

1. Branch from the default `dev`; keep each change focused and target its pull request at `dev`. Dependabot also targets `dev`. Release to protected `main` only through a pull request from this repository's `dev`, after all required checks pass. Direct pushes, force pushes and deletion of `main` are disabled, including for administrators. No approval count is required for the solo-maintainer workflow, but review conversations must be resolved.
2. Write runtime instructions and contributor documentation in English. Keep README.ru.md aligned with the English user guide. Keep multilingual reader utterances in evaluation fixtures so language adaptation remains testable.
3. Preserve the distinction between reader preferences and facts about a system. Keep history reads bounded and restricted to the current user.
4. Add or improve a meaningful evaluation when explanation behavior changes. Compare in fresh contexts; keep expectations hidden from executors.
5. Run the local checks and report unavailable CLI or rendering checks accurately.
6. Describe the problem, resulting behavior and evidence in the pull request. Use the existing template.

Contributions to human-please and its new maintenance files are under the MIT license. Independent sibling projects keep their existing terms. No CLA is required. Keep real transcripts, profiles, credentials and generated evaluation runs out of contributions.

## Conduct

Be respectful and specific. Critique explanations and evidence, not a reader's intelligence, age or disability. Harassment and disclosure of private information are unacceptable. Maintainers may remove harmful content and restrict participation.
