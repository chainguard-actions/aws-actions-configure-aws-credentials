<!-- markdownlint-disable -->

# Hardening Report: aws-actions--configure-aws-credentials/v6.1.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **aws-actions--configure-aws-credentials/v6.1.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

Every `uses:` reference across all workflow files uses a mutable tag, branch, or version string instead of a pinned 40-character commit SHA. This exposes the workflows to supply-chain attacks if any referenced action is compromised or its tag is moved.

Failing references include:
- automerge-approved-prs.yml: `aws-actions/configure-aws-credentials@v6`, `aws-actions/aws-secretsmanager-get-secrets@v2`
- cawsc-test.yml: `aws-actions/configure-aws-credentials@main` (branch ref — especially dangerous)
- close-stale-issues.yml: `aws-actions/stale-issue-cleanup@v6`
- closed-issue-message.yml: `aws-actions/closed-issue-message@v1`
- dependabot-autoapprove.yml: `dependabot/fetch-metadata@v2`, `actions/checkout@v5`, `aws-actions/configure-aws-credentials@v6`, `aws-actions/aws-secretsmanager-get-secrets@v2`
- handle-stale-discussions.yml: `aws-github-ops/handle-stale-discussions@v1`
- issue-regression-labeler.yml: `actions/github-script@v7`
- package-dist.yml: `actions/checkout@v5`, `aws-actions/configure-aws-credentials@v6`, `aws-actions/aws-secretsmanager-get-secrets@v2`
- pull-request-lint.yml: `amannn/action-semantic-pull-request@v5.5.3`
- release-please.yml: `actions/checkout@v5`, `aws-actions/configure-aws-credentials@v6`, `aws-actions/aws-secretsmanager-get-secrets@v2`, `googleapis/release-please-action@v4`
- tests-integ-push.yml: `actions/checkout@v5`
- tests-integ-release.yml: `actions/checkout@v5` (multiple), `actions/github-script@v8`
- tests-unit.yml: `actions/checkout@v5`, `actions/setup-node@v4.4.0`, `actions/setup-node@v4`, `bahmutov/npm-install@v1`

Locations:

- `.github/workflows/automerge-approved-prs.yml:13`
- `.github/workflows/cawsc-test.yml:11`
- `.github/workflows/close-stale-issues.yml:16`
- `.github/workflows/closed-issue-message.yml:9`
- `.github/workflows/dependabot-autoapprove.yml:14`
- `.github/workflows/handle-stale-discussions.yml:16`
- `.github/workflows/issue-regression-labeler.yml:14`
- `.github/workflows/package-dist.yml:20`
- `.github/workflows/pull-request-lint.yml:16`
- `.github/workflows/release-please.yml:16`
- `.github/workflows/tests-integ-push.yml:17`
- `.github/workflows/tests-integ-release.yml:22`
- `.github/workflows/tests-unit.yml:16`

### script-injection (severity: high)

Multiple `run:` blocks directly interpolate `${{ ... }}` expressions into shell command strings (sub-rule a), allowing an attacker to inject arbitrary shell commands.

**issue-regression-labeler.yml** — The 'Manage regression label' step interpolates `${{ steps.check_regression.outputs.is_regression }}`, `${{ github.event.issue.number }}`, and `${{ github.repository }}` directly into a shell `if` statement and `gh issue edit` commands. The issue number and repository values are attacker-influenced via the `issues: [opened, edited]` trigger.

**package-dist.yml** — The 'Commit' step interpolates `${{ env.OSDS_ACCESS_TOKEN }}` directly into shell commands: `echo "::add-mask::${{ env.OSDS_ACCESS_TOKEN }}"` and `git remote set-url origin https://${{ env.OSDS_ACCESS_TOKEN }}@github.com/...`. Any expression inside a `run:` block is a script-injection risk regardless of context.

**tests-integ-release.yml** — The 'create and mask access key' step interpolates `${{ runner.os }}` directly into a shell command: `aws iam create-access-key --user-name integ-test-static-user-${{ runner.os }}`. The 'delete access key' step also interpolates `${{ runner.os }}` and `${{ steps.create-key.outputs.STATIC_ACCESS_KEY_ID }}` directly into shell commands.

Locations:

- `.github/workflows/issue-regression-labeler.yml:27`
- `.github/workflows/package-dist.yml:39`
- `.github/workflows/tests-integ-release.yml:57`
- `.github/workflows/tests-integ-release.yml:70`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses, script-injection

**Notes:**

Fixed all 13 workflow files with unpinned action references by pinning to full 40-character commit SHAs (preserving original tags as comments). Fixed script injection in 3 workflow files (issue-regression-labeler.yml, package-dist.yml, tests-integ-release.yml) by moving all ${{ }} expressions out of run: shell strings and into step env: blocks, referencing them as plain environment variables in the shell scripts. Specific SHAs pinned: actions/checkout@fbc6f3992d24b796d5a048ff273f7fcc4a7b6c09 (v5), actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020 (v4/v4.4.0), actions/github-script@f28e40c7f34bde8b3046d885e986cb6290c5673b (v7), actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd (v8), aws-actions/configure-aws-credentials@517a711dbcd0e402f90c77e7e2f81e849156e31d (v6), aws-actions/configure-aws-credentials@9d2a1c17c0d020ee966ed3fa5e24c290d759b4fa (main), aws-actions/aws-secretsmanager-get-secrets@a9a7eb4e2f2871d30dc5b892576fde60a2ecc802 (v2), aws-actions/stale-issue-cleanup@7de35968489e4142233d2a6812519a82e68b5c38 (v6), aws-actions/closed-issue-message@cf797c2463fa6b95a23b2957fe075a3fa9aa8138 (v1), dependabot/fetch-metadata@21025c705c08248db411dc16f3619e6b5f9ea21a (v2), aws-github-ops/handle-stale-discussions@711a9813957be17629fc6933afcd8bd132c57254 (v1), amannn/action-semantic-pull-request@0723387faaf9b38adef4775cd42cfd5155ed6017 (v5.5.3), googleapis/release-please-action@5c625bfb5d1ff62eadeeb3772007f7f66fdcf071 (v4), bahmutov/npm-install@20216767ca67f0f7b4d095dc5859c5700a6581cb (v1).

