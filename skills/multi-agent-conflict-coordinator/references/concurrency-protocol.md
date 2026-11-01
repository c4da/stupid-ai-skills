# Agent File Lease & Mutex Protocol

## State Transition Lifecycle

1. **Unclaimed**: Any agent may acquire an exclusive lease on a file path for up to 120 seconds (default 60s).
2. **Leased(agent_id, session_id, expires_at)**:
   - Modifications by the lease owner update the lease TTL and trigger CAS pre-image snapshots.
   - Attempted writes by a different agent receive `409 ConflictBlocked` with lease metadata and decomposition guidance.
3. **Released(agent_id)**: Explicitly released when the agent finishes its diff or commits the decision to the ledger.
4. **Expired**: If an agent hangs, crashes, or times out, the lease lapses safely, preventing distributed deadlocks.
