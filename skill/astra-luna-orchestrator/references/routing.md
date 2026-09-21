# Native Codex model selection

The installed setup has three separate jobs:

1. Codex selects the Astra root and child models.
2. The standalone custom role pins the child model and reasoning effort.
3. This skill tells Astra when to plan, delegate, review, and integrate.

The worker is the native Codex model `gpt-5.6-luna` at `xhigh`. There is no
proxy route, model catalog, external worker CLI, or generated routing binding.
The installer leaves root settings, provider configuration,
authentication, permissions, and `config.toml` untouched.

## Installation bindings

The installer creates `$CODEX_HOME/agents/astra_luna_builder.toml` with its own
model and effort. It does not require, inherit, or change global
`[agents].default_subagent_model` or
`[agents].default_subagent_reasoning_effort` values, so unrelated agents keep
their existing defaults.

The role omits sandbox settings so it inherits the parent sandbox and approvals.
Its `[agents].enabled = false` setting prevents recursive subagent tools.

## Runtime check

Fully quit and reopen the host app, start a session with Astra selected, and
check that the installed skill and role are visible. Run `scripts/doctor.py`
with the same CODEX_HOME/profile used by the session.

Inspect the actual session and project/CLI/UI/managed overrides. If the client
does not load standalone personal agent TOML files or expose native subagent
tools, stop delegation and identify the incompatibility. Do not write legacy
configuration keys based on guesswork or fall back to another model.

For the first real delegated task, verify all of the following:

- The root thread still shows Astra.
- The child thread/session metadata shows `gpt-5.6-luna` at `xhigh`.
- The child executes a small useful task, changes only its scope, and returns
  test evidence; Astra reviews the result independently.

When metadata is unavailable, report that runtime model selection remains
unverified. A response saying "I am GPT-5.6 Luna" is not evidence. Do not run a
paid probe as part of package installation; the first approved useful task can
establish runtime evidence.

## Usage and privacy

Delegation sends the selected task context and tool results through the host's
configured native OpenAI path. Preserve privacy restrictions on private
repositories; use minimal necessary context and avoid production data and
secrets. A worktree is not an operating-system sandbox. Do not disable approval
or sandbox mechanisms or use a bypass-permissions CLI.

Record observed usage only when available. This package cannot promise a
specific usage reduction, price, latency, quality ranking, or maximum runtime.
