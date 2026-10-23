# Automated Dependency Updates - Demo

Demo project for TechAbout task ZR-26-00755 (Task 8): automatic dependency
update pull requests with GitHub Dependabot.

## What is set up

- `requirements.txt` pins two dependencies to deliberately old versions
  (`requests==2.25.1`, `python-dateutil==2.8.1`) so the bot has real updates
  to propose.
- `.github/dependabot.yml` tells Dependabot to check the pip ecosystem daily
  and open update pull requests (max 5 open at once, commit prefix `deps`,
  label `dependencies`).
- Dependabot opens a PR for each outdated dependency. A human reviews and
  merges; the bot never merges on its own in this setup.

## Files

- `.github/dependabot.yml` - the Dependabot configuration
- `requirements.txt` / `app.py` - the sample project
- `REVIEWING.md` - how the team should review bot pull requests
- `RUNBOOK.md` - setup and operations notes

## Proof

See the Pull Requests tab of this repository: the update PRs there were
created by `dependabot[bot]`, not by a human.
