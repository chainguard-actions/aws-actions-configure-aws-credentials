<!-- markdownlint-disable -->

# Hardening Report: aws-actions--configure-aws-credentials/v6.2.4

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **aws-actions--configure-aws-credentials/v6.2.4** was hardened automatically. 4 finding(s) were identified and resolved across 3 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): Multiple ${{ }} expressions are interpolated directly inside run: shell commands. In the 'Manage regression label' step, ${{ steps.check_regression.outputs.is_regression }}, ${{ github.event.issue.number }}, and ${{ github.repository }} are embedded directly in shell commands. An attacker who controls issue content could inject arbitrary shell commands via github.event.issue.number or github.repository.

Locations:

- `.github/workflows/issue-regression-labeler.yml:24`

### script-injection (severity: high)

Sub-rule (a): Multiple ${{ }} expressions are interpolated directly inside run: shell commands. In the 'Tag Major Version' step, ${{ env.OSDS_ACCESS_TOKEN }}, ${{ steps.release.outputs.major }}, and ${{ steps.release.outputs.tag_name }} are embedded directly in shell commands (e.g., 'git remote set-url origin https://${{ env.OSDS_ACCESS_TOKEN }}@github.com/...'). In the 'Update README version references' step, ${{ steps.release.outputs.tag_name }} and ${{ env.OSDS_ACCESS_TOKEN }} are also interpolated directly into shell commands.

Locations:

- `.github/workflows/release-please.yml:47`
- `.github/workflows/release-please.yml:60`

### script-injection (severity: high)

Sub-rule (a): ${{ env.OSDS_ACCESS_TOKEN }} is interpolated directly inside a run: shell command in the 'Commit' step: 'git remote set-url origin https://${{ env.OSDS_ACCESS_TOKEN }}@github.com/aws-actions/configure-aws-credentials.git'. Any expression inside ${{ }} is subject to YAML template substitution before the shell sees it, making this a script-injection risk.

Locations:

- `.github/workflows/package-dist.yml:36`

### unpinned-uses (severity: high)

All uses: references across all workflow files use mutable tag or branch refs instead of immutable 40-character SHA digests, making the workflows vulnerable to supply-chain attacks if any referenced action is compromised or its tag is moved. Failing references include: aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2, actions/checkout@v5, dependabot/fetch-metadata@v2, aws-actions/stale-issue-cleanup@v7, aws-actions/closed-issue-message@v1, aws-github-ops/handle-stale-discussions@v1, actions/github-script@v7, actions/github-script@v8, googleapis/release-please-action@v4, amannn/action-semantic-pull-request@v5.5.3, actions/setup-node@v6.4.0, actions/setup-node@v4, bahmutov/npm-install@v1, aws-actions/configure-aws-credentials@main.

Locations:

- `.github/workflows/automerge-approved-prs.yml:13`
- `.github/workflows/automerge-approved-prs.yml:17`
- `.github/workflows/cawsc-test.yml:11`
- `.github/workflows/close-stale-issues.yml:14`
- `.github/workflows/closed-issue-message.yml:9`
- `.github/workflows/dependabot-autoapprove.yml:14`
- `.github/workflows/dependabot-autoapprove.yml:16`
- `.github/workflows/dependabot-autoapprove.yml:19`
- `.github/workflows/dependabot-autoapprove.yml:23`
- `.github/workflows/handle-stale-discussions.yml:13`
- `.github/workflows/issue-regression-labeler.yml:12`
- `.github/workflows/package-dist.yml:18`
- `.github/workflows/package-dist.yml:25`
- `.github/workflows/package-dist.yml:30`
- `.github/workflows/pull-request-lint.yml:14`
- `.github/workflows/release-please.yml:16`
- `.github/workflows/release-please.yml:20`
- `.github/workflows/release-please.yml:28`
- `.github/workflows/release-please.yml:35`
- `.github/workflows/release-please.yml:41`
- `.github/workflows/tests-integ-push.yml:16`
- `.github/workflows/tests-integ-release.yml:22`
- `.github/workflows/tests-integ-release.yml:57`
- `.github/workflows/tests-integ-release.yml:134`
- `.github/workflows/tests-integ-release.yml:172`
- `.github/workflows/tests-integ-release.yml:218`
- `.github/workflows/tests-integ-release.yml:264`
- `.github/workflows/tests-integ-release.yml:271`
- `.github/workflows/tests-integ-release.yml:315`
- `.github/workflows/tests-unit.yml:14`
- `.github/workflows/tests-unit.yml:16`
- `.github/workflows/tests-unit.yml:27`
- `.github/workflows/tests-unit.yml:29`
- `.github/workflows/tests-unit.yml:32`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, unpinned-uses

**Notes:**

Fixed all 3 script-injection findings by moving ${{ }} expressions from run: shell blocks into step env: blocks and referencing them as plain environment variables. Fixed all 35 unpinned-uses findings across 13 workflow files by pinning every action reference to its full 40-character SHA digest (with the original tag preserved as a comment). Files modified: issue-regression-labeler.yml, release-please.yml, package-dist.yml, automerge-approved-prs.yml, cawsc-test.yml, close-stale-issues.yml, closed-issue-message.yml, dependabot-autoapprove.yml, handle-stale-discussions.yml, pull-request-lint.yml, tests-integ-push.yml, tests-integ-release.yml, tests-unit.yml.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed two script injection vulnerabilities in .github/workflows/tests-integ-release.yml:
1. 'create and mask access key' step (line 62): Moved ${{ runner.os }} to an env: block as RUNNER_OS_NAME, replaced inline expression with $RUNNER_OS_NAME in the shell command.
2. 'delete access key' step (line 89): Moved both ${{ runner.os }} and ${{ steps.create-key.outputs.STATIC_ACCESS_KEY_ID }} to an env: block as RUNNER_OS_NAME and STATIC_ACCESS_KEY_ID respectively, replaced inline expressions with $RUNNER_OS_NAME and "$STATIC_ACCESS_KEY_ID" in the shell command.

### Iteration 3

**Fixes applied:** script-injection

**Notes:**

Fixed two unquoted $RUNNER_OS_NAME expansions in .github/workflows/tests-integ-release.yml. In the `create and mask access key` step (line ~64) and the `delete access key` step (line ~92), changed `integ-test-static-user-$RUNNER_OS_NAME` to `integ-test-static-user-"$RUNNER_OS_NAME"` to prevent shell word splitting and glob expansion on the variable value.

