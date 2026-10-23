# How the team should review Dependabot pull requests

Dependabot PRs are real code changes to the project's supply chain. Review
them like any other PR, with a few dependency-specific checks.

## The 2-minute checklist

1. **Read the PR body.** Dependabot includes the release notes and changelog
   links for the new version. Skim for "breaking change", "removed", or
   "deprecated" - major version bumps (for example 2.x to 3.x) deserve a full
   read, minor and patch bumps usually do not.
2. **Check it is the version you expect.** Confirm the from/to versions in the
   title (example: `deps: bump requests from 2.25.1 to 2.32.5`) and that the
   diff only touches the dependency file (requirements.txt / lock file).
   A Dependabot PR should never change application code.
3. **Require green CI.** Never merge a dependency update with failing tests.
   If CI fails, the new version likely broke something: do not force it,
   comment `@dependabot ignore this major version` if needed and fix
   compatibility in a separate human PR.
4. **Merge promptly.** Small, frequent updates are the point of the setup.
   A PR that sits for weeks defeats it and lets the next bump grow bigger.
   Patch and minor updates with green CI can be merged the same day.
5. **One at a time.** Merge bot PRs one by one, not in a batch, so if
   something breaks in production you know exactly which update caused it.

## Commands you can comment on a Dependabot PR

- `@dependabot rebase` - rebuild the PR on top of the latest main.
- `@dependabot recreate` - close and reopen a fresh PR.
- `@dependabot ignore this major version` - stop proposing that major bump.
- `@dependabot ignore this dependency` - stop all PRs for that package.

## Security updates

Dependabot also raises **security update** PRs when a dependency has a known
vulnerability. Treat those as urgent: review and merge the same day, ahead of
regular version updates.
