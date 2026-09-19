# GitHub configuration

The dump validation workflow lives at:

- **Intended path:** `.github/workflows/validate-dump.yml`
- **Checked-in source (same YAML):** [`ci/validate-dump.github-actions.yml`](../ci/validate-dump.github-actions.yml)

The OAuth token used by automation lacked the `workflow` scope, so the live Actions path must be created by copying that file to `.github/workflows/validate-dump.yml` (GitHub UI or a token with `workflow` scope). Until then, run `npm run build:dump && npm run validate:dump` locally.
