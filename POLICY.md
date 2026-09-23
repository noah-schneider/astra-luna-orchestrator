<!-- BEGIN astra-luna-orchestrator managed policy -->
## Astra-led planning and delegated implementation

For substantial builds, multi-file features, migrations, or refactors, load
`$astra-luna-orchestrator`, `$astra-sol-orchestrator`, or
`$astra-solx-orchestrator` before implementation.
Keep GPT-6 Astra as the root planner, architect, reviewer, and integrator.
Default to the Luna skill unless the user invokes or requests Sol or Solx.
The Luna skill uses `astra_luna_builder` pinned to GPT-6 Luna at max;
the Sol skill uses `astra_sol_builder` pinned to GPT-6 Sol at high;
the Solx skill uses `astra_solx_builder` pinned to GPT-6 Sol at xhigh.
Use one worker from the invoked skill by default; do not create an agent for
each tiny coding step.
Prefer this native workflow over an older external-runner skill for the same task;
do not load both execution paths.

Thin-root orchestration is the only supported delegated workflow; there is no
mode selector or alternate full-Astra orchestration setting. After establishing
the contract, give one worker a coherent end-to-end phase bundle and let it own
repository discovery,
implementation, testing, debugging, and routine browser/visual QA inside that
scope. Astra should normally perform one planning batch, one dispatch, one wait,
one batched acceptance review, and one final response. Do not poll for progress,
request status updates, interrupt a healthy run, duplicate the worker's repository
work, or rerun its full validation without a concrete reason.

This is a scoped exception to generic personal defaults such as "one agent" or
"no workers" in this instruction file. Keep those defaults for trivial changes,
unrelated work, and tasks explicitly requested without delegation. It does not
supersede a current user prohibition, repository restrictions, or managed policy.
A worker child executes its assigned brief; it must not load the orchestration
workflow or delegate further.

Reuse an existing approved spec/plan, including Superpowers or GSD artifacts.
Otherwise establish scope and contracts, plan dependency-ordered phases, then
execute and review each task bundle. Review specification compliance and quality/
security as two lenses in one batched pass. Send all findings in one correction
request and default to at most one correction cycle. Do not repeat approval
questions already resolved by the user's instruction. Material scope changes still
need resolution. Keep final review and sensitive architecture decisions with Astra.

Additional Astra investigation or verification is justified for a concrete
architecture, security, authorization, payments, tenancy, secrets, destructive
migration, production, or shared-infrastructure risk. High assurance is an
exception triggered by evidence, not the routine operating mode.

Do not switch the root to a worker model, silently fall back to a different
worker model,
launch another agent CLI, loosen permissions, expose secrets, auto-commit,
push, deploy, or start paid setup smoke tests. Normal delegated implementation
uses the native worker model pinned by the invoked skill; obey the user's
data-sharing and spending
restrictions. Installation is not evidence of successful delegated inference.
<!-- END astra-luna-orchestrator managed policy -->
