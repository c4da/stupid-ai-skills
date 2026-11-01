# Anti-Monolith Decomposition for Concurrent Agents

## Why Monoliths Attract Merge Conflicts

When a team of agents works in a repository, 80% of merge conflicts happen in:
- Central toolbar files (`toolbar.rs`)
- Top-level routers (`routes.rs`, `handlers.rs`)
- Root coordinator modules (`mod.rs`, `index.ts`)

These files act as "God Files" where every new tool demands an edit.

## The Feature-per-File Solution

Instead of editing the shared file:
1. Create a dedicated child file for your specific tool:
   - `src/cad/toolbar/fillet_tool.rs`
   - `src/cad/toolbar/chamfer_tool.rs`
   - `src/cad/toolbar/extrude_tool.rs`
2. Encapsulate all UI structs, callbacks, and validation within that child file.
3. Keep the shared coordinator strictly as an API gateway:
   - Only exports submodules (`pub mod fillet_tool;`)
   - Dispatches via enum matching without holding raw implementation logic.
4. By doing this, multiple agents can build 10 different tools concurrently with **zero line overlap**!
