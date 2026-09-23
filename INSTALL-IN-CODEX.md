# Install using Codex

Give Codex the location of this repository and the prompt below. This authorization covers only installation, not a real delegated task.

```text
Install the Astra + GPT-6 Luna, GPT-6 Sol, and GPT-6 Sol xhigh skills for Codex from this repository.

Pin gpt-6-luna at max, gpt-6-sol at high, and gpt-6-sol at xhigh in separate native roles. Do not infer or auto-select a
billing provider.

Read README.md, install.py, POLICY.md and WORKER-INSTRUCTIONS.md first.
Inspect relevant local configuration without printing secrets, authentication
contents or unrelated instructions.

Preserve my current root model and reasoning effort, config.toml,
authentication, permissions and unrelated instructions. Do not install another
runtime or dependencies, restart services, or quit Codex.
Do not add, change or remove [agents].default_subagent_model or
[agents].default_subagent_reasoning_effort. The package's named roles pin their
own worker models and efforts.

Verify Python 3.11+ and native subagent/custom-role client support. The named
roles must pin gpt-6-luna at max and gpt-6-sol at high and xhigh.
The default python3 may be older than 3.11; find an existing 3.11+ interpreter
such as python3.12 and use it for every command here. Do not install or upgrade a
runtime to satisfy this.
If configuration is contradictory or unsupported, report the discrepancy.
Do not silently change models/providers or bypass preflight.
Never edit config.toml to make a preflight check pass. Report the discrepancy and
stop. Appending a table header such as [agents] to config.toml absorbs every
top-level key written after it and can stop Codex loading its config at all.

Do not ask me to paste a key into chat, inspect credential contents, or enter a key
for me. Do not run subagents certify, test-model --live, a smoke test or any other
paid inference command during installation.

Run the offline tests, then install.py for a dry run. If they pass and the
proposed files match the documented scope, apply with install.py --apply.
I authorize installation of all three personal skills, native astra_luna_builder,
astra_sol_builder, and astra_solx_builder roles,
and scoped managed AGENTS policy exception. Retain repository restrictions,
explicit no-delegation instructions and managed security controls.

The roles must pin GPT-6 Luna at max and GPT-6 Sol at high and xhigh, inherit sandbox/approvals and disable nested agents.
Do not invoke an external worker CLI. Run the static doctor after installation.
If the current root is a worker model, select Astra in a new session before
delegating and rerun the doctor; installation itself preserves the root.

Verify config/auth files and existing permissions are unchanged and unrelated
policy content is preserved. Report installed paths, root/worker settings,
test results, undo receipt and remaining runtime limitations.

Do not launch workers, run paid inference, commit, push or deploy during setup.
Explain that I should fully quit/reopen the host app and start an Astra session and invoke
$astra-luna-orchestrator, $astra-sol-orchestrator, or $astra-solx-orchestrator. Actual model-selection verification belongs to the first
separately authorized useful task, using host/session metadata.
```
