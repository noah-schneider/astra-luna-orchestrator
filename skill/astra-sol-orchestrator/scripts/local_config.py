#!/usr/bin/env python3
"""Read-only inspection of an existing native Codex setup; no model requests."""
from __future__ import annotations

import hashlib
import os
import re
import sys
from pathlib import Path

if sys.version_info < (3, 11):
    raise SystemExit("Python 3.11+ is required. No packages or settings were changed.")
import tomllib

WORKER_MODEL = "gpt-6-sol"
WORKER_EFFORT = "high"
ROLE = "astra_sol_builder"
SKILL = "astra-sol-orchestrator"

# Keys Codex reads as scalar settings directly under [agents]. Every other key
# there is read as an agent NAME whose value must be a role table, so a scalar
# under an unrecognized name makes Codex reject the entire config with
# "invalid type: ..., expected struct AgentRoleToml in `agents`" -- which takes
# down the host app and the CLI together, not just subagent routing.
AGENT_SCALAR_SETTINGS = frozenset({
    "enabled",
    "default_subagent_model",
    "default_subagent_reasoning_effort",
    "interrupt_message",
    "max_concurrent_threads_per_session",
    "max_threads",
    "max_depth",
    "job_max_runtime_seconds",
})


class SetupError(ValueError):
    """An actionable configuration problem, without credential-bearing details."""


def read_toml(path: Path) -> dict:
    try:
        with path.open("rb") as stream:
            return tomllib.load(stream)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        # TOML errors can embed source text. Never echo them or a full config.
        raise SetupError(f"Cannot read valid TOML from {path.name} ({type(exc).__name__}).") from None


def merge_tables(base: dict, overlay: dict) -> dict:
    result = dict(base)
    for key, value in overlay.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = merge_tables(result[key], value)
        else:
            result[key] = value
    return result


def inspect(
    home: Path,
    codex_home: Path,
    profile: str | None = None,
    allow_worker_root: bool = False,
) -> dict:
    """Return a redacted static report for the native Codex setup."""
    config_path = codex_home / "config.toml"
    config = read_toml(config_path)
    input_hashes = {str(config_path): hashlib.sha256(config_path.read_bytes()).hexdigest()}
    selected = profile if profile is not None else config.get("profile")
    warnings: list[str] = []
    if selected:
        if not isinstance(selected, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", selected):
            raise SetupError("Unsupported profile name; inspect the active profile manually.")
        standalone = codex_home / f"{selected}.config.toml"
        legacy = config.get("profiles", {}).get(selected)
        if standalone.exists() and legacy is not None:
            raise SetupError("Both standalone and legacy profile definitions exist; resolve that ambiguity first.")
        if standalone.exists():
            config = merge_tables(config, read_toml(standalone))
            input_hashes[str(standalone)] = hashlib.sha256(standalone.read_bytes()).hexdigest()
        elif isinstance(legacy, dict):
            config = merge_tables(config, legacy)
            warnings.append("A legacy inline profile was inspected; confirm your client still applies it.")
        else:
            raise SetupError("The selected profile is not available as a readable configuration file.")

    agents = config.get("agents", {})
    if not isinstance(agents, dict):
        raise SetupError("The existing [agents] setting is not a TOML table.")
    # Checking shape rather than a list of known top-level names catches any
    # absorbed key, not just the handful an installer happens to anticipate.
    misplaced = sorted(
        key for key, value in agents.items()
        if key not in AGENT_SCALAR_SETTINGS and not isinstance(value, dict)
    )
    if misplaced:
        raise SetupError(
            "Setting(s) that do not belong under [agents] were found there: "
            + ", ".join(misplaced)
            + ". In TOML, a table header remains active until the next table header, so a "
            "top-level key written after [agents] is absorbed into it; Codex then reads that "
            "key as an agent name and refuses to load the whole config. Move those keys above "
            "the first table header, or under the agent role they belong to, before installing. "
            "If your Codex build documents one of them as a genuine [agents] setting, it is newer "
            "than this check; verify with `codex doctor` rather than editing around this error."
        )
    if agents.get("enabled") is False:
        raise SetupError("Subagents are disabled in the inspected config. This installer will not enable them silently.")
    if "default_subagent_model" in agents:
        warnings.append(
            "The global default_subagent_model is not used or changed; the installed named role pins its own worker model."
        )
    worker_root = config.get("model") in {"gpt-6-luna", "openai/gpt-6-luna", "gpt-6-sol", "openai/gpt-6-sol"}
    if worker_root:
        if not allow_worker_root:
            raise SetupError("The root model is a worker model. Select Astra as root before using this workflow.")
        warnings.append("The current root is a worker model; select Astra before delegating. Installation leaves the root unchanged.")
    if not config.get("model"):
        warnings.append("No root model is set in this config; select GPT-6 Astra in the new session UI.")
    if config.get("features", {}).get("multi_agent") is False:
        warnings.append("A legacy features.multi_agent=false flag exists; check whether your client honors it.")
    warnings.append("Project, CLI, UI and managed-policy overrides, plus runtime custom-role support, are not resolved by this static inspection.")
    report = {
        "status": "install-ready" if worker_root else "static-ready",
        "runtime_verified": False,
        "inference_request_made": False,
        "root_model_observed": config.get("model"),
        "root_effort_observed": config.get("model_reasoning_effort"),
        "worker_model": WORKER_MODEL,
        "worker_effort": WORKER_EFFORT,
        "custom_agent": ROLE,
        "profile_inspected": selected,
        "native_custom_role": True,
        "input_hashes": input_hashes,
        "warnings": warnings,
    }
    return report


def default_locations(home_arg: str | None = None, codex_home_arg: str | None = None) -> tuple[Path, Path]:
    home = Path(home_arg).expanduser().resolve() if home_arg else Path.home().resolve()
    codex_home = Path(codex_home_arg or os.environ.get("CODEX_HOME", str(home / ".codex"))).expanduser().absolute()
    return home, codex_home
