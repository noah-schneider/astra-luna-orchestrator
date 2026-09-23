# Validation evidence

Unreleased candidate based on version 1.2.0. Checked September 23, 2026 on
Windows with Python 3.14.7.

## Verified

- 48 offline tests passed. Coverage includes installation dry runs, idempotence,
  original configuration preservation, scoped policy handling,
  profile/collision/symlink checks, fake-secret redaction,
  generated role TOML, rollback, guarded undo, plan validation and release-file
  filtering.
- The generated native roles pin GPT-6 Luna at `max` and GPT-6 Sol at `high` or `xhigh`,
  and leave global child
  defaults, root settings and `config.toml` unchanged.
- Existing backup-directory permissions are preserved.
- Backup files and caches are excluded from skill installation. Release tests also cover private artifact exclusion, symlink rejection and inventory changes.

All three skill entrypoints passed a local frontmatter check. The Luna example and
converted Sol and Solx plans passed their respective structure validators. The skill-creator
validator could not run because this Python environment lacks PyYAML.

All tests use synthetic configuration and temporary directories. They do not require a provider account or invoke model inference. Python 3.11 is the minimum supported syntax/runtime target, but this release's local suite was run on 3.14.7; other versions and operating systems have not been tested here.

## Prior local installation evidence

The preceding package revision was installed in a macOS Codex setup using an Astra root and a native worker role. Static configuration checks passed; root configuration and authentication bytes were preserved. The public revision's installer is verified with synthetic homes; this report does not claim it was reapplied to that real installation.

## Still unverified

Actual delegated inference, native role loading in a fresh session, long-running
build quality and cost savings remain unverified for this candidate. A static
report or a worker naming itself cannot establish these facts.

Validate real model selection during the first authorized useful task, using
host/session metadata. Do not run an extra paid test as part of installation, and
do not publish raw private logs or local configuration as evidence.
