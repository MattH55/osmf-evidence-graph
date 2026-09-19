# GitHub configuration

CI workflow: [`.github/workflows/validate-dump.yml`](workflows/validate-dump.yml)

On every push and pull request it runs `npm ci`, `npm run build:dump`, and `npm run validate:dump` against `schemas/dump.bundled.schema.json`.

A duplicate copy is kept at [`ci/validate-dump.github-actions.yml`](../ci/validate-dump.github-actions.yml) for reference.
