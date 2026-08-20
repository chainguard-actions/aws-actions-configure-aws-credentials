<!-- markdownlint-disable -->

# Hardening Report: aws-actions--configure-aws-credentials/v6.0.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **aws-actions--configure-aws-credentials/v6.0.0** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): GitHub Actions expressions are directly interpolated inside run: shell commands. In issue-regression-labeler.yml, the 'Manage regression label' step interpolates ${{ steps.check_regression.outputs.is_regression }}, ${{ github.event.issue.number }}, and ${{ github.repository }} directly into shell commands. An attacker could craft an issue number or repository value to inject shell metacharacters. These values should be passed via env: variables and then referenced as quoted shell variables (e.g., "$ISSUE_NUMBER").

Locations:

- `.github/workflows/issue-regression-labeler.yml:25`
- `.github/workflows/issue-regression-labeler.yml:26`
- `.github/workflows/issue-regression-labeler.yml:28`

### script-injection (severity: high)

Sub-rule (a): GitHub Actions expressions are directly interpolated inside run: shell commands. In package-dist.yml, the 'Commit' step interpolates ${{ env.OSDS_ACCESS_TOKEN }} directly into shell commands: `echo "::add-mask::${{ env.OSDS_ACCESS_TOKEN }}"` and `git remote set-url origin https://${{ env.OSDS_ACCESS_TOKEN }}@github.com/...`. Any expression inside ${{ }} is substituted before the shell sees the string, bypassing shell quoting. The token should be passed via an env: variable and referenced as "$OSDS_ACCESS_TOKEN".

Locations:

- `.github/workflows/package-dist.yml:38`
- `.github/workflows/package-dist.yml:40`

### unpinned-uses (severity: high)

All uses: references across workflow files use mutable tags or branch names instead of pinned 40-character SHA digests, making the workflows vulnerable to supply-chain attacks if any referenced action is compromised or its tag is moved. Failing references include: actions/checkout@v5, actions/setup-node@v4.4.0, actions/setup-node@v4, actions/github-script@v7, aws-actions/configure-aws-credentials@v5, aws-actions/aws-secretsmanager-get-secrets@v2, aws-actions/stale-issue-cleanup@v6, aws-actions/closed-issue-message@v1, aws-github-ops/handle-stale-discussions@v1, dependabot/fetch-metadata@v2, bahmutov/npm-install@v1, amannn/action-semantic-pull-request@v5.5.3, and aws-actions/configure-aws-credentials@main.

Locations:

- `.github/workflows/automerge-approved-prs.yml:14`
- `.github/workflows/automerge-approved-prs.yml:18`
- `.github/workflows/cawsc-test.yml:10`
- `.github/workflows/close-stale-issues.yml:17`
- `.github/workflows/closed-issue-message.yml:9`
- `.github/workflows/dependabot-autoapprove.yml:16`
- `.github/workflows/dependabot-autoapprove.yml:17`
- `.github/workflows/dependabot-autoapprove.yml:20`
- `.github/workflows/dependabot-autoapprove.yml:24`
- `.github/workflows/handle-stale-discussions.yml:13`
- `.github/workflows/issue-regression-labeler.yml:13`
- `.github/workflows/package-dist.yml:19`
- `.github/workflows/package-dist.yml:29`
- `.github/workflows/package-dist.yml:33`
- `.github/workflows/pull-request-lint.yml:15`
- `.github/workflows/tests-integ-push.yml:17`
- `.github/workflows/tests-integ-release.yml:16`
- `.github/workflows/tests-integ-release.yml:33`
- `.github/workflows/tests-integ-release.yml:52`
- `.github/workflows/tests-integ-release.yml:72`
- `.github/workflows/tests-integ-release.yml:97`
- `.github/workflows/tests-integ-release.yml:122`
- `.github/workflows/tests-integ-release.yml:126`
- `.github/workflows/tests-unit.yml:16`
- `.github/workflows/tests-unit.yml:18`
- `.github/workflows/tests-unit.yml:28`
- `.github/workflows/tests-unit.yml:30`
- `.github/workflows/tests-unit.yml:33`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, unpinned-uses

**Notes:**

Fixed all three findings:

1. script-injection in issue-regression-labeler.yml: Moved ${{ steps.check_regression.outputs.is_regression }}, ${{ github.event.issue.number }}, and ${{ github.repository }} into the step's env: block as IS_REGRESSION, ISSUE_NUMBER, and REPOSITORY. Shell script now uses quoted "$IS_REGRESSION", "$ISSUE_NUMBER", "$REPOSITORY".

2. script-injection in package-dist.yml: Moved ${{ env.OSDS_ACCESS_TOKEN }} into the step's env: block as TOKEN. Shell script now uses $TOKEN.

3. unpinned-uses: Pinned all 13 distinct action references across 10 workflow files to full 40-character SHA digests, preserving original tag names in comments. Actions pinned: actions/checkout@v5, actions/setup-node@v4.4.0 and @v4, actions/github-script@v7, aws-actions/configure-aws-credentials@v5 and @main, aws-actions/aws-secretsmanager-get-secrets@v2, aws-actions/stale-issue-cleanup@v6, aws-actions/closed-issue-message@v1, aws-github-ops/handle-stale-discussions@v1, dependabot/fetch-metadata@v2, bahmutov/npm-install@v1, amannn/action-semantic-pull-request@v5.5.3.

