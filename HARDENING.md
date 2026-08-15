<!-- markdownlint-disable -->

# Hardening Report: aws-actions--configure-aws-credentials/v6.2.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **aws-actions--configure-aws-credentials/v6.2.1** was hardened automatically. 16 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Direct ${{ }} expression interpolation inside run: shell commands. In issue-regression-labeler.yml, the 'Manage regression label' step interpolates ${{ steps.check_regression.outputs.is_regression }}, ${{ github.event.issue.number }}, and ${{ github.repository }} directly into shell commands, allowing an attacker to inject arbitrary shell code via a crafted issue number or repository name. Rule (a) violated.

Locations:

- `.github/workflows/issue-regression-labeler.yml:27`
- `.github/workflows/issue-regression-labeler.yml:28`

### script-injection (severity: high)

Direct ${{ }} expression interpolation inside run: shell commands. In package-dist.yml, the 'Commit' step interpolates ${{ env.OSDS_ACCESS_TOKEN }} directly into a git remote URL and an echo command inside the run: block. Any workflow-controlled env context value is substituted before the shell parses the command. Rule (a) violated.

Locations:

- `.github/workflows/package-dist.yml:38`
- `.github/workflows/package-dist.yml:41`

### script-injection (severity: high)

Direct ${{ }} expression interpolation inside run: shell commands. In release-please.yml, the 'Tag Major Version' step interpolates ${{ steps.release.outputs.major }} directly into git commands, and the 'Update README version references' step interpolates ${{ steps.release.outputs.tag_name }} into a sed command and ${{ env.OSDS_ACCESS_TOKEN }} into a git remote URL — all inside run: blocks. Rule (a) violated.

Locations:

- `.github/workflows/release-please.yml:53`
- `.github/workflows/release-please.yml:54`
- `.github/workflows/release-please.yml:55`
- `.github/workflows/release-please.yml:57`
- `.github/workflows/release-please.yml:61`
- `.github/workflows/release-please.yml:65`
- `.github/workflows/release-please.yml:67`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests, making the workflow vulnerable to supply-chain attacks if the referenced action is compromised or its tag is moved. Unpinned references: uses: aws-actions/configure-aws-credentials@v6, uses: aws-actions/aws-secretsmanager-get-secrets@v2.

Locations:

- `.github/workflows/automerge-approved-prs.yml:13`
- `.github/workflows/automerge-approved-prs.yml:17`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags/branches instead of pinned 40-character SHA digests. Unpinned reference: uses: aws-actions/configure-aws-credentials@main (branch reference — highest risk).

Locations:

- `.github/workflows/cawsc-test.yml:11`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned reference: uses: aws-actions/stale-issue-cleanup@v6.

Locations:

- `.github/workflows/close-stale-issues.yml:15`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned reference: uses: aws-actions/closed-issue-message@v1.

Locations:

- `.github/workflows/closed-issue-message.yml:10`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned references: uses: dependabot/fetch-metadata@v2, uses: actions/checkout@v5, uses: aws-actions/configure-aws-credentials@v6, uses: aws-actions/aws-secretsmanager-get-secrets@v2.

Locations:

- `.github/workflows/dependabot-autoapprove.yml:14`
- `.github/workflows/dependabot-autoapprove.yml:16`
- `.github/workflows/dependabot-autoapprove.yml:18`
- `.github/workflows/dependabot-autoapprove.yml:22`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned reference: uses: aws-github-ops/handle-stale-discussions@v1.

Locations:

- `.github/workflows/handle-stale-discussions.yml:13`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned reference: uses: actions/github-script@v7.

Locations:

- `.github/workflows/issue-regression-labeler.yml:13`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned references: uses: actions/checkout@v5, uses: aws-actions/configure-aws-credentials@v6, uses: aws-actions/aws-secretsmanager-get-secrets@v2.

Locations:

- `.github/workflows/package-dist.yml:19`
- `.github/workflows/package-dist.yml:30`
- `.github/workflows/package-dist.yml:35`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned reference: uses: amannn/action-semantic-pull-request@v5.5.3.

Locations:

- `.github/workflows/pull-request-lint.yml:16`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned references: uses: actions/checkout@v5 (×2), uses: aws-actions/configure-aws-credentials@v6, uses: aws-actions/aws-secretsmanager-get-secrets@v2, uses: googleapis/release-please-action@v4.

Locations:

- `.github/workflows/release-please.yml:17`
- `.github/workflows/release-please.yml:22`
- `.github/workflows/release-please.yml:27`
- `.github/workflows/release-please.yml:32`
- `.github/workflows/release-please.yml:44`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned reference: uses: actions/checkout@v5.

Locations:

- `.github/workflows/tests-integ-push.yml:17`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned references: uses: actions/checkout@v5 (multiple), uses: actions/github-script@v8.

Locations:

- `.github/workflows/tests-integ-release.yml:20`
- `.github/workflows/tests-integ-release.yml:57`
- `.github/workflows/tests-integ-release.yml:100`
- `.github/workflows/tests-integ-release.yml:138`
- `.github/workflows/tests-integ-release.yml:175`
- `.github/workflows/tests-integ-release.yml:205`
- `.github/workflows/tests-integ-release.yml:233`
- `.github/workflows/tests-integ-release.yml:261`

### unpinned-uses (severity: high)

All uses: references in this workflow use mutable version tags instead of pinned 40-character SHA digests. Unpinned references: uses: actions/checkout@v5, uses: actions/setup-node@v6.4.0, uses: actions/setup-node@v4, uses: bahmutov/npm-install@v1.

Locations:

- `.github/workflows/tests-unit.yml:15`
- `.github/workflows/tests-unit.yml:17`
- `.github/workflows/tests-unit.yml:27`
- `.github/workflows/tests-unit.yml:30`
- `.github/workflows/tests-unit.yml:33`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, unpinned-uses

**Notes:**

Fixed all 3 script-injection findings by moving ${{ }} expressions from run: shell commands into step env: blocks and referencing them as plain shell variables. Fixed all unpinned-uses findings across 11 workflow files by pinning every action reference to its full 40-character SHA digest (preserving the original tag/branch in a comment). All SHAs were resolved using lookup_action_sha.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed two script injection vulnerabilities in .github/workflows/tests-integ-release.yml in the static_assumeRole job:
1. 'create and mask access key' step (line 62): Moved ${{ runner.os }} into an env block as RUNNER_OS_NAME and referenced it as $RUNNER_OS_NAME in the shell command.
2. 'delete access key' step (line 87): Moved both ${{ runner.os }} and ${{ steps.create-key.outputs.STATIC_ACCESS_KEY_ID }} into an env block as RUNNER_OS_NAME and STATIC_ACCESS_KEY_ID respectively, and referenced them as environment variables in the shell command. Both values are now properly double-quoted in the shell commands.

