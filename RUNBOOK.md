# Runbook: Dependabot Setup

## How it was set up

1. Created the repository with a normal `requirements.txt` (versions pinned,
   deliberately old to demonstrate real updates).
2. Added `.github/dependabot.yml`:

   ```yaml
   version: 2
   updates:
     - package-ecosystem: "pip"
       directory: "/"
       schedule:
         interval: "daily"
       open-pull-requests-limit: 5
       commit-message:
         prefix: "deps"
       labels:
         - "dependencies"
   ```

3. That file is all it takes: once it lands on the default branch, GitHub
   enables Dependabot version updates for the repo automatically. No secrets,
   tokens, or third-party apps are needed.

## Changing the setup

- **Cadence**: change `schedule.interval` to `weekly` or `monthly` if daily
  PRs are too noisy. Weekly is a good default for most team repos.
- **Other ecosystems**: add another `updates` entry with
  `package-ecosystem: "npm"` (or `docker`, `github-actions`, `maven`, and
  others) and its directory.
- **Grouping**: for repos with many dependencies, add a `groups` block so
  minor and patch updates arrive as one grouped PR instead of many.
- **Auto-merge**: not enabled here on purpose. If the team wants it later,
  it can be turned on for patch updates only, after CI is trusted.

## Troubleshooting

- **No PRs appear**: check the repo's Insights tab, Dependency graph, and
  that `dependabot.yml` is valid YAML on the default branch. Also check
  Settings, Code security, Dependabot version updates is on.
- **Too many PRs**: lower `open-pull-requests-limit` or switch to weekly.
- **A PR keeps failing CI**: see REVIEWING.md; ignore that major version and
  handle the upgrade as planned human work.
