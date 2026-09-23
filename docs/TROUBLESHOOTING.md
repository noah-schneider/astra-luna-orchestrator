# Troubleshooting

## The skill is missing

Check that installation ended with `Installed` or `Already installed`, not only a successful dry run. The expected files are `~/.agents/skills/astra-luna-orchestrator/SKILL.md`, `~/.agents/skills/astra-sol-orchestrator/SKILL.md`, and `~/.agents/skills/astra-solx-orchestrator/SKILL.md`. Fully quit/reopen the host app, then start an Astra session. Check custom home locations and client skill discovery before reinstalling.

## Worker role is unavailable

The installed role must be visible under `$CODEX_HOME/agents/` and the client must
support native subagents. Fully quit/reopen the host app, start a new Astra
session, and run the static doctor again. Do not fall back to another model or
write legacy configuration keys based on guesswork.

## Custom role is unavailable in a new session

The installed client must support standalone personal agent TOML files and expose native delegation. Files on disk do not prove the running tool supports them. Check your installed client and project/managed overrides. Do not fall back to a different model or external agent CLI.

## Existing skill or role conflicts

The installer refuses symlinked targets, duplicate skill locations and differing package-owned files. Review existing content before using `--replace`; keep the resulting receipt. Do not remove unrelated skills to resolve discovery.

## Undo refuses because a file changed

This protects later edits, including changes to the shared personal AGENTS file. Preserve those edits, compare the receipt and backup locally, then reconcile deliberately. Do not publish receipts or original instruction backups.

## No savings or quality guarantee

Provider usage and real task outcomes determine cost and quality. Offline tests validate installation and planning helpers, not the performance of either model. Session metadata is model-selection evidence; a worker's self-description is not.

## A worker is visible but delegation is unavailable

Confirm the invoked skill's role pins `gpt-6-luna` at `max` or `gpt-6-sol`
at `high` or `xhigh`, that subagents are enabled, and
that no project, CLI, UI or managed-policy override replaces the role. Runtime
metadata from a small useful task is the only evidence of actual child-model
selection; a worker's self-description is not.
