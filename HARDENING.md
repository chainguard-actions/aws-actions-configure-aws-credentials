<!-- markdownlint-disable -->

# Hardening Report: aws-actions--configure-aws-credentials/v6.2.3

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **aws-actions--configure-aws-credentials/v6.2.3** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

Multiple workflow files reference actions using mutable tags or branch names instead of full 40-character SHA commit hashes, making them vulnerable to supply-chain attacks if the referenced tag is moved or the branch is updated.

Failing references:
- automerge-approved-prs.yml: aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2
- cawsc-test.yml: aws-actions/configure-aws-credentials@main
- close-stale-issues.yml: aws-actions/stale-issue-cleanup@v6
- closed-issue-message.yml: aws-actions/closed-issue-message@v1
- dependabot-autoapprove.yml: dependabot/fetch-metadata@v2, actions/checkout@v5, aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2
- handle-stale-discussions.yml: aws-github-ops/handle-stale-discussions@v1
- issue-regression-labeler.yml: actions/github-script@v7
- package-dist.yml: actions/checkout@v5, aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2
- pull-request-lint.yml: amannn/action-semantic-pull-request@v5.5.3
- release-please.yml: actions/checkout@v5, aws-actions/configure-aws-credentials@v6, aws-actions/aws-secretsmanager-get-secrets@v2, googleapis/release-please-action@v4
- tests-integ-push.yml: actions/checkout@v5
- tests-integ-release.yml: actions/checkout@v5, actions/github-script@v8
- tests-unit.yml: actions/checkout@v5, actions/setup-node@v6.4.0, bahmutov/npm-install@v1, actions/setup-node@v4

Locations:

- `.github/workflows/automerge-approved-prs.yml:12`
- `.github/workflows/cawsc-test.yml:11`
- `.github/workflows/close-stale-issues.yml:16`
- `.github/workflows/closed-issue-message.yml:10`
- `.github/workflows/dependabot-autoapprove.yml:14`
- `.github/workflows/handle-stale-discussions.yml:14`
- `.github/workflows/issue-regression-labeler.yml:13`
- `.github/workflows/package-dist.yml:19`
- `.github/workflows/pull-request-lint.yml:17`
- `.github/workflows/release-please.yml:18`
- `.github/workflows/tests-integ-push.yml:16`
- `.github/workflows/tests-integ-release.yml:20`
- `.github/workflows/tests-unit.yml:14`

### script-injection (severity: high)

Multiple run: blocks directly interpolate ${{ }} expressions into shell commands (rule a), allowing an attacker to inject arbitrary shell commands.

1. issue-regression-labeler.yml — 'Manage regression label' step interpolates ${{ steps.check_regression.outputs.is_regression }}, ${{ github.event.issue.number }}, and ${{ github.repository }} directly into shell commands:
   `if [ "${{ steps.check_regression.outputs.is_regression }}" == "true" ]; then`
   `gh issue edit ${{ github.event.issue.number }} --add-label "potential-regression" -R ${{ github.repository }}`

2. package-dist.yml — 'Commit' step interpolates ${{ env.OSDS_ACCESS_TOKEN }} directly into shell commands:
   `echo "::add-mask::${{ env.OSDS_ACCESS_TOKEN }}"`
   `git remote set-url origin https://${{ env.OSDS_ACCESS_TOKEN }}@github.com/...`

3. release-please.yml — 'Tag Major Version' and 'Update README version references' steps interpolate ${{ env.OSDS_ACCESS_TOKEN }}, ${{ steps.release.outputs.major }}, and ${{ steps.release.outputs.tag_name }} directly into shell commands:
   `echo "::add-mask::${{ env.OSDS_ACCESS_TOKEN }}"`
   `git remote set-url origin https://${{ env.OSDS_ACCESS_TOKEN }}@github.com/...`
   `if git rev-parse "v${{ steps.release.outputs.major }}" > /dev/null 2>&1; then`
   `sed -i 's|...|configure-aws-credentials@${{ steps.release.outputs.tag_name }}|g' README.md`

4. tests-integ-release.yml — 'create and mask access key' and 'delete access key' steps interpolate ${{ runner.os }} and ${{ steps.create-key.outputs.STATIC_ACCESS_KEY_ID }} directly into shell commands:
   `AK_OUTPUT=$(aws iam create-access-key --user-name integ-test-static-user-${{ runner.os }})`
   `aws iam delete-access-key --user-name integ-test-static-user-${{ runner.os }} --access-key-id ${{ steps.create-key.outputs.STATIC_ACCESS_KEY_ID }}`

Locations:

- `.github/workflows/issue-regression-labeler.yml:23`
- `.github/workflows/package-dist.yml:35`
- `.github/workflows/release-please.yml:50`
- `.github/workflows/release-please.yml:63`
- `.github/workflows/tests-integ-release.yml:50`
- `.github/workflows/tests-integ-release.yml:65`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses, script-injection

**Notes:**

Fixed all 13 workflow files with unpinned action references by pinning each to its full 40-character SHA commit hash (with original tag/branch preserved as a comment). Fixed script injection in 4 workflow files (issue-regression-labeler.yml, package-dist.yml, release-please.yml, tests-integ-release.yml) by moving all ${{ }} expressions out of run: blocks into step-level env: blocks and referencing them as plain environment variables in the shell scripts.

