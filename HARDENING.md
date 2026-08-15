<!-- markdownlint-disable -->

# Hardening Report: aws-actions--configure-aws-credentials/v4.3.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **aws-actions--configure-aws-credentials/v4.3.1** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

Multiple workflow files reference actions using mutable tag or branch refs instead of pinned 40-character SHA commits, making them vulnerable to supply-chain attacks. Affected refs include: actions/checkout@v4, actions/setup-node@v4, bahmutov/npm-install@v1, aws-actions/configure-aws-credentials@v4, aws-actions/configure-aws-credentials@main, aws-actions/stale-issue-cleanup@v6, aws-actions/closed-issue-message@v1, aws-actions/aws-secretsmanager-get-secrets@v2, dependabot/fetch-metadata@v2, aws-github-ops/handle-stale-discussions@v1, actions/github-script@v7, amannn/action-semantic-pull-request@v5.5.3, googleapis/release-please-action@v4.

Locations:

- `.github/workflows/automerge-approved-prs.yml:14`
- `.github/workflows/automerge-approved-prs.yml:19`
- `.github/workflows/cawsc-test.yml:10`
- `.github/workflows/close-stale-issues.yml:16`
- `.github/workflows/closed-issue-message.yml:9`
- `.github/workflows/dependabot-autoapprove.yml:14`
- `.github/workflows/dependabot-autoapprove.yml:16`
- `.github/workflows/dependabot-autoapprove.yml:18`
- `.github/workflows/dependabot-autoapprove.yml:23`
- `.github/workflows/handle-stale-discussions.yml:14`
- `.github/workflows/issue-regression-labeler.yml:13`
- `.github/workflows/package-dist.yml:18`
- `.github/workflows/package-dist.yml:27`
- `.github/workflows/package-dist.yml:32`
- `.github/workflows/pull-request-lint.yml:14`
- `.github/workflows/release-please.yml:14`
- `.github/workflows/release-please.yml:19`
- `.github/workflows/release-please.yml:24`
- `.github/workflows/release-please.yml:29`
- `.github/workflows/tests-unit.yml:16`
- `.github/workflows/tests-unit.yml:19`
- `.github/workflows/tests-unit.yml:21`
- `.github/workflows/tests-unit.yml:31`
- `.github/workflows/tests-unit.yml:34`
- `.github/workflows/tests-unit.yml:36`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation inside run: shell commands. In issue-regression-labeler.yml, the 'Manage regression label' step interpolates ${{ steps.check_regression.outputs.is_regression }}, ${{ github.event.issue.number }}, and ${{ github.repository }} directly inside shell commands (e.g., `if [ "${{ steps.check_regression.outputs.is_regression }}" == "true" ]` and `gh issue edit ${{ github.event.issue.number }} --add-label ... -R ${{ github.repository }}`). An attacker could craft an issue number or repository value to inject shell commands. In package-dist.yml, the 'Commit' step interpolates ${{ env.OSDS_ACCESS_TOKEN }} directly inside a shell command (`git remote set-url origin https://${{ env.OSDS_ACCESS_TOKEN }}@github.com/...`), which is a template-substituted value that bypasses shell quoting.

Locations:

- `.github/workflows/issue-regression-labeler.yml:25`
- `.github/workflows/issue-regression-labeler.yml:26`
- `.github/workflows/issue-regression-labeler.yml:28`
- `.github/workflows/package-dist.yml:38`

### missing-permissions (severity: medium)

The workflow file tests-unit.yml has no top-level permissions: key, and neither of its two jobs (unit-test and lint) defines a job-level permissions: block. Without explicit permissions, the GITHUB_TOKEN is granted default (potentially broad) permissions, violating the principle of least privilege.

Locations:

- `.github/workflows/tests-unit.yml:1`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses, script-injection, missing-permissions

**Notes:**

Fixed all three findings across 9 workflow files:

1. unpinned-uses: Pinned all 13 unique action references to full 40-char SHAs with tag comments preserved. Files updated: automerge-approved-prs.yml, cawsc-test.yml, close-stale-issues.yml, closed-issue-message.yml, dependabot-autoapprove.yml, handle-stale-discussions.yml, issue-regression-labeler.yml, package-dist.yml, pull-request-lint.yml, release-please.yml, tests-unit.yml.

2. script-injection: In issue-regression-labeler.yml, moved ${{ steps.check_regression.outputs.is_regression }}, ${{ github.event.issue.number }}, and ${{ github.repository }} into the step env block (IS_REGRESSION, ISSUE_NUMBER, REPOSITORY) and referenced them as plain shell variables. In package-dist.yml, moved ${{ env.OSDS_ACCESS_TOKEN }} into the step env block and referenced it as $OSDS_ACCESS_TOKEN.

3. missing-permissions: Added top-level `permissions: contents: read` to tests-unit.yml to enforce least privilege for the pull_request workflow.

