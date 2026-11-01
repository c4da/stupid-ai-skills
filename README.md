# 🌟 Agensi.io Skills Marketplace

> **The Official Skill Catalog & Distribution Repository for [Agensi.io](https://agensi.io)**  
> Universal, versioned skills, personas, and coordination modules for AI coding agents (Claude Code, Cursor, Windsurf, Antigravity, GitHub Copilot CLI, Hermes).

---

## 🎯 Architecture & Separation

This repository houses the **curated skill distribution catalog** for Agensi.io, separate from the underlying runtime engine:

- **[AgentTrace](https://github.com/c4da/agent_trace)**: Open-source, compiled Rust runtime firewall, pre-image CAS rollback guard, and cryptographic ledger.
- **[Agensi Skills](https://github.com/agensi-io/agensi-skills)**: Distributable agent capabilities, engineering guardrails, multi-agent coordination protocols, and roleplay personas.

Every skill is standalone, human-readable in markdown (`SKILL.md`), cryptographically signed with a SHA-256 hash in its `manifest.json`, and compatible across 20+ agent environments.

---

## 📦 Catalog Overview

### 🛡️ Enterprise & Runtime Safety (Powered by AgentTrace)

| Skill | Tier | Description | Provenance SHA-256 |
| :--- | :---: | :--- | :--- |
| **`agent-runtime-firewall`** | `Free` | Pre-flight safety checks, destructive command interception, DLP secret redaction, and instant Pre-Image CAS rollback. | `1e95d3f4...` |
| **`local-model-offload`** | `Free` | Zero-token local offloading for tests, boilerplate, and audits via Ollama/Hermes to save external API tokens. | `4a0bf71f...` |
| **`agent-decision-ledger`** | `Free` | SHA-256 tamper-evident milestone logging, architectural decision records, and cryptographic proof verification. | `a705c33d...` |
| **`multi-agent-conflict-coordinator`** | `Paid` | Eliminates split-brain collisions when multiple agents edit the same shared file (toolbars, routers) via dynamic leases and anti-monolith feature decomposition. | `6fb0c135...` |

---

### 🎭 Fun, Personas & Roleplay

| Skill | Tier | Description | Provenance SHA-256 |
| :--- | :---: | :--- | :--- |
| **`talk-like-yoda`** | `Free` | Compels the agent to speak with the authentic grammar (OSV inversion), cadence, and ancient wisdom of Jedi Master Yoda. *"Strong with the borrow checker, this code is."* | `dc37b6ce...` |
| **`talk-like-tech-priest`** | `Free` | Harsh, uncompromising Adeptus Mechanicus Tech-Priest (Warhammer 40K). Berates fleshly weakness, purges heretical scrapcode, and demands pure liturgy of the Machine God. | `cc85554a...` |
| **`talk-like-pirate`** | `Free` | Swashbuckling pirate captain persona. Code reviews become ocean voyages, bugs are the Kraken, and refactoring is swabbing the deck! | `89898636...` |
| **`cyberpunk-netrunner`** | `Free` | Gritty Neuromancer / Cyberpunk 2077 netrunner persona. Neural jacks, military black ICE countermeasures, and data fortress sweeps. | `70378a2e...` |

---

## ⚡ How to Install & Use Skills

### Option A: Antigravity IDE & Built-in Agents
Copy the desired skill folder to your `.gemini/antigravity/skills/` or workspace `.agents/skills/`:
```bash
git clone https://github.com/agensi-io/agensi-skills.git
cp -r agensi-skills/skills/talk-like-yoda ~/.gemini/antigravity/skills/
```

### Option B: Claude Code & Claude Desktop
Add to your Claude Code commands or import as a skill prompt:
```bash
claude skill install skills/talk-like-yoda
```

### Option C: Cursor & Windsurf
Include the `SKILL.md` content in your `.cursorrules` or `.windsurfrules`.

---

## 🛠️ Validation & Provenance

To verify the cryptographic integrity of all skills:
```bash
python tools/validate_catalog.py
```
This ensures all `SKILL.md` documents match their registered SHA-256 checksums in `registry.json`.

---

## 📄 License
MIT OR Apache-2.0. See individual skill manifests for specifics.
