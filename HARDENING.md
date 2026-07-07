<!-- markdownlint-disable -->

# Hardening Report: aws-actions--configure-aws-credentials/v6.2.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `1`

Action **aws-actions--configure-aws-credentials/v6.2.2** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

Multiple workflow files reference actions using mutable tag or branch refs instead of pinned 40-character SHA digests, making them vulnerable to supply-chain attacks. Failing refs include: automerge-approved-prs.yml: aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2; cawsc-test.yml: aws-actions/configure-aws-credentials@main; close-stale-issues.yml: aws-actions/stale-issue-cleanup@v6; closed-issue-message.yml: aws-actions/closed-issue-message@v1; dependabot-autoapprove.yml: dependabot/fetch-metadata@v2, actions/checkout@v5, aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2; handle-stale-discussions.yml: aws-github-ops/handle-stale-discussions@v1; issue-regression-labeler.yml: actions/github-script@v7; package-dist.yml: actions/checkout@v5, aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2; pull-request-lint.yml: amannn/action-semantic-pull-request@v5.5.3; release-please.yml: actions/checkout@v5, aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2, googleapis/release-please-action@v4; tests-integ-push.yml: actions/checkout@v5; tests-integ-release.yml: actions/checkout@v5, actions/github-script@v8; tests-unit.yml: actions/checkout@v5, actions/setup-node@v6.4.0, actions/setup-node@v4, bahmutov/npm-install@v1.

Locations:

- `.github/workflows/automerge-approved-prs.yml:12`
- `.github/workflows/cawsc-test.yml:11`
- `.github/workflows/close-stale-issues.yml:16`
- `.github/workflows/closed-issue-message.yml:10`
- `.github/workflows/dependabot-autoapprove.yml:13`
- `.github/workflows/handle-stale-discussions.yml:14`
- `.github/workflows/issue-regression-labeler.yml:14`
- `.github/workflows/package-dist.yml:20`
- `.github/workflows/pull-request-lint.yml:17`
- `.github/workflows/release-please.yml:19`
- `.github/workflows/tests-integ-push.yml:18`
- `.github/workflows/tests-integ-release.yml:21`
- `.github/workflows/tests-unit.yml:19`

### script-injection (severity: high)

Rule (a) violation: ${{ ... }} expressions are interpolated directly inside run: shell command strings. In issue-regression-labeler.yml, the 'Manage regression label' run block uses ${{ steps.check_regression.outputs.is_regression }}, ${{ github.event.issue.number }}, and ${{ github.repository }} directly in shell commands (e.g. 'gh issue edit ${{ github.event.issue.number }} --add-label ...'). In package-dist.yml, the 'Commit' run block uses ${{ env.OSDS_ACCESS_TOKEN }} directly in shell commands (e.g. 'git remote set-url origin https://${{ env.OSDS_ACCESS_TOKEN }}@github.com/...'). In release-please.yml, the 'Tag Major Version' and 'Update README version references' run blocks use ${{ steps.release.outputs.major }}, ${{ steps.release.outputs.tag_name }}, and ${{ env.OSDS_ACCESS_TOKEN }} directly in shell commands. In tests-integ-release.yml, the 'create and mask access key' run block uses ${{ runner.os }} and the 'delete access key' run block uses ${{ runner.os }} and ${{ steps.create-key.outputs.STATIC_ACCESS_KEY_ID }} directly in shell commands.

Locations:

- `.github/workflows/issue-regression-labeler.yml:28`
- `.github/workflows/package-dist.yml:40`
- `.github/workflows/release-please.yml:55`
- `.github/workflows/tests-integ-release.yml:57`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses, script-injection

**Notes:**

Fixed all 13 workflow files with unpinned action references by replacing mutable tags/branches with pinned 40-character SHA digests (with tag comments for readability). Fixed script injection in 4 files (issue-regression-labeler.yml, package-dist.yml, release-please.yml, tests-integ-release.yml) by moving all ${{ }} expressions out of run: shell strings into env: blocks and referencing them as plain environment variables. Specific SHAs used: actions/checkout@v5=93cb6efe, aws-actions/configure-aws-credentials@v6=517a711d, aws-actions/aws-secretsmanager-get-secrets@v2=a9a7eb4e, aws-actions/stale-issue-cleanup@v6=7de35968, aws-actions/closed-issue-message@v1=cf797c24, dependabot/fetch-metadata@v2=21025c70, aws-github-ops/handle-stale-discussions@v1=711a9813, actions/github-script@v7=f28e40c7, actions/github-script@v8=ed597411, amannn/action-semantic-pull-request@v5.5.3=0723387f, googleapis/release-please-action@v4=5c625bfb, actions/setup-node@v6.4.0=48b55a01, actions/setup-node@v4=49933ea5, bahmutov/npm-install@v1=20216767.

