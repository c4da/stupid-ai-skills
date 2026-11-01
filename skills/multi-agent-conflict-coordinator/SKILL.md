---
name: multi-agent-conflict-coordinator
description: Detects, coordinates, and resolves multi-agent file contention, concurrent edits, and split-brain race conditions when multiple agents (Copilot, Cursor, Antigravity, subagents) work on the same codebase simultaneously. Replaces passive "wait it out" deadlocks with deterministic file leases, anti-monolith feature decomposition, and telemetry handoffs.
license: MIT OR Apache-2.0
compatibility: Compatible with all coding agents. Interfaces with AgentTrace Gateway (>= 1.1.0) via MCP or HTTP API for atomic file leases.
metadata:
  author: agensi.io
  version: "1.0.0"
  categories: ["coordination", "multi-agent", "developer-tools", "concurrency"]
  tags: ["concurrency", "multi-agent", "mutex", "file-locks", "copilot", "git-conflicts"]
---

# 🚦 Multi-Agent Conflict Coordinator

> *"I notice there are multiple agents editing the same construction toolbar, which is causing conflicts. That sounds tricky, and I recognize we need to be patient and wait this out..."* &mdash; Uncoordinated Agent

Autonomous coding agents working in parallel often attempt to edit the same coordinator, UI toolbar, or router file simultaneously. Standard LLMs lack concurrency primitives and default to **polite helplessness** (passive waiting) or **silent clobbering** (blindly overwriting concurrent edits).

This skill provides the **Deterministic Agent Concurrency Protocol**, turning passive waiting into proactive, non-blocking modular engineering.

---

## 🚫 The Anti-Pattern: Polite Helplessness

When two agents collide on a file:
- ❌ Do **NOT** say: *"Let's be patient and wait this out."*
- ❌ Do **NOT** overwrite the file hoping the other agent's changes weren't important.
- ❌ Do **NOT** sit in a sleep loop burning tokens.

---

## ⚡ The 3-Step Coordination Protocol

```
                        Concurrent Edit Detected
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
   File Lock Available?                      File Contested / Locked
              │                                         │
   ┌──────────┴──────────┐                   ┌──────────┴──────────┐
   ▼                     ▼                   ▼                     ▼
Acquire Lease       Execute Edit        Decompose to          Queue via
  (60s TTL)         & Release           New Submodule         Handoff Bundle
```

### Step 1: Pre-Flight File Lease Check
Before initiating edits on shared files (e.g. `toolbar.rs`, `router.rs`, `mod.rs`, `main.rs`), check if a lease is active:
- **MCP**: Call `check_file_lease(path)` or `acquire_file_lease(path, ttl_seconds: 60)`.
- **CLI/HTTP**:
  ```bash
  python scripts/agenttrace.py check_lease --path "src/cad/toolbar.rs"
  ```

If granted, proceed immediately with the edit.

### Step 2: The Non-Blocking Decomposition Rule (Feature-per-File)
If the target file is **currently locked by another agent** (e.g., Copilot is editing `src/cad/toolbar.rs`):

**NEVER WAIT. Decompose your feature into a dedicated, isolated file.**

1. **Create Feature File**: Instead of adding your tool into `toolbar.rs`, create a new submodule:
   `src/cad/toolbar/my_new_tool.rs`
2. **Implement Independently**: Author the entire feature, tests, and math inside `my_new_tool.rs` without touching `toolbar.rs`.
3. **Minimal Coordinator Touchpoint**: When the lease expires or is released, only a single non-conflicting line is added to the coordinator:
   ```rust
   pub mod my_new_tool;
   ```
   Or wait for the other agent to finish and submit a clean 1-line registration diff.

### Step 3: Telemetry Handoff Exchange
If the work is strictly sequential and depends on the other agent's partial output:
1. Query AgentTrace for the active session's handoff bundle:
   ```bash
   python scripts/agenttrace.py get_telemetry_handoff --session-id <other-session>
   ```
2. Inspect the other agent's latest CAS diff and committed decision hash.
3. Build directly on top of the verified diff rather than starting from stale disk state.

---

## 🛡️ Resolving 409 Conflict Responses from AgentTrace

When AgentTrace Gateway returns `409 Conflict`:
```json
{
  "verdict": "ConflictBlocked",
  "resource": "src/cad/toolbar.rs",
  "locked_by": "copilot-agent-01",
  "lease_ttl_remaining_ms": 32000,
  "guidance": "DecomposeIntoSubmodule"
}
```

The agent must:
1. Log the conflict notice to the user:
   > *"Notice: `src/cad/toolbar.rs` is currently leased by `copilot-agent-01`. In accordance with Feature-per-File architecture, creating `src/cad/toolbar/construction_tools.rs` to proceed in parallel without blocking."*
2. Implement the feature in the isolated submodule.
3. Run headless unit tests to verify the submodule in isolation.

---

## 🔍 References

- [references/concurrency-protocol.md](references/concurrency-protocol.md) &mdash; Detailed state diagram of distributed agent file leases.
- [references/anti-monolith-decomposition.md](references/anti-monolith-decomposition.md) &mdash; Guidelines for splitting shared files into conflict-free submodules.
