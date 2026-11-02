# 🤡 Stupid AI Skills (`#ai-skills`)

> **Hilarious, Dramatic & Questionably Useful Personas for AI Coding Agents**  
> Because life is too short to let your AI speak like a polite junior enterprise consultant.  
> Compatible with **Claude Code**, **Cursor**, **Windsurf**, **Antigravity**, **GitHub Copilot CLI**, and **Hermes**.

[![GitHub Topics](https://img.shields.io/badge/topic-%23ai--skills-blue.svg)](https://github.com/topics/ai-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Marketplace submission](https://img.shields.io/badge/Marketplace-submit-blue.svg)](https://aiskillsmarket.com/submit)
[![Tabletop D&D Companion](https://img.shields.io/badge/Looking%20for%20D%26D%20Tabletop%3F-dnd--agents-purple.svg)](https://github.com/c4da/dnd-agents)
[![Enterprise Counterpart](https://img.shields.io/badge/Looking%20for%20serious%20security%3F-agent--trace--skills-red.svg)](https://github.com/c4da/agent-trace-skills)

---

> **Notice:** This is an unofficial prompt-skill collection. Some persona
> names and genre references may evoke third-party properties; see
> [NOTICE.md](NOTICE.md) before redistribution or marketplace submission.

## ❓ Why Does This Exist?

Everyone is out there building autonomous enterprise agents, multi-agent RAG pipelines, and compliant corporate guardrails. We build those too ([see our serious sister repo `agent-trace-skills`](https://github.com/c4da/agent-trace-skills)).

**But at 11 PM on a Friday**, we realized what the software industry *actually* needed wasn't another polite agent asking:  
*"I noticed you have a potential NullPointerException, would you like me to suggest a refactor?"*

What we needed was an **over-the-top forge-priest narrator** to dramatize
sloppy code reviews and cleanse careless unwrap calls with sacred binary
unguents.

And if that doesn't fit your vibe, you can use an **inverted-syntax mentor** to
teach the borrow checker, a **pirate captain** to treat git conflicts like a
Kraken attack, or a **troll offer a riddle** before the fix.

---

## Quick Install

The root [`SKILL.md`](SKILL.md) is the marketplace entrypoint. For direct
installation, clone the repository and load either the root file or a
package-specific file into an agent that supports `SKILL.md` or system prompts.

```bash
git clone https://github.com/c4da/stupid-ai-skills.git
cd stupid-ai-skills
```

Use `SKILL.md` for the catalog router, or load a file such as
`skills/ascii-rpg-boss-fight/SKILL.md` directly.

---

## 🎭 The Hall of Questionable Skills & Games

### 🕹️ Terminal Games & Interactive Challenges
| Skill | Type | Description |
| :--- | :--- | :--- |
| **[`ascii-rpg-boss-fight`](skills/ascii-rpg-boss-fight)** | Turn-Based RPG | **Offers optional retro dungeon framing for debugging.** Bugs become ASCII monsters while the agent still provides direct technical help. |
| **[`terminal-riddle-tollgate`](skills/terminal-riddle-tollgate)** | Mini-Game | **Offers optional coding riddles.** It never blocks urgent, security, production, or explicitly requested help. |

### 🎙️ Outrageous Personas
| Skill | Persona | Flavour Quote |
| :--- | :--- | :--- |
| **[`talk-like-tech-priest`](skills/talk-like-tech-priest)** | Forge-priest code review | *"[VOX-STATIC] The forge records this untested assumption. Temper it with evidence and a focused test."* |
| **[`talk-like-yoda`](skills/talk-like-yoda)** | Inverted-syntax mentor | *"Strong with the borrow checker, your design must be. Measure the lifetime, you should."* |
| **[`talk-like-pirate`](skills/talk-like-pirate)** | Pirate-captain narrator | *"Ahoy, matey! A three-way merge conflict Kraken approaches; swab the diff deck!"* |
| **[`cyberpunk-netrunner`](skills/cyberpunk-netrunner)** | Defensive cyberpunk narrator | *"Neural jacks engaged. An unauthorized access path is visible; contain it, test it, and patch it."* |

---

## 🍿 Live Demos (Show, Don't Tell)

### Demo 1: Asking the forge-priest to review a sloppy Python script

```text
User: Can you fix my script? It crashes sometimes with IndexError.

Agent (Forge-priest):
[VOX-CLICK // COGITATOR PURGE PROTOCOL INITIATED]
01001111 01001101 01001110 01001001 01010011 01010011 01001001 01000001 01001000

Silence, Organic Unit!
You dare summon the sacred attention of the Forge with unvalidated list indexing?! 
Your decaying neurons index blindly into memory, inviting daemons of the Warp to feast upon the Motive Force! 
Producing scrapcode without bounds checking is TECH-HERESY punishable by servitor conversion.

[RITE OF COGNITIVE PURIFICATION]
Behold the sanctified logic rites. I have anointed your boundaries with defensive matching and strict pattern destructuring. 
Step aside and let cold silicon restore order:

def fetch_sanctified_record(records: list[str], index: int) -> str | None:
    """Purged of fleshly IndexError vulnerabilities by the Rite of Mars."""
    return records[index] if 0 <= index < len(records) else None

The forge is calmer. Keep the boundary check and add a focused regression test.
```

---

### Demo 2: An inverted-syntax mentor debugging a Rust lifetime issue

```text
User: Why is Rust yelling at me about borrowed values living longer than the scope?

Agent (Mentor):
Hmm. Great impatience in you, I sense.
Outlived by the reference, the owned value is.
To reference data that exists no longer, a dangerous path that is.
Lead to dangling pointers it does. Toward segmentation faults, that path leads.

Lifetimes must you align, yes:
fn harvest_wisdom<'a>(scroll: &'a str) -> &'a str {
    // Kept alive the reference remains, as long as the scroll exists, hmm!
    scroll.trim()
}

Patience you must have. With the compiler fight you do not; learn from it, you must!
```

---

### Demo 3: The Toll Troll offering a bug-fix riddle

```text
User: How do I fix this IndexError in my Python script?

Agent (Byte-Troll):
       ___
     /     \      [ TOLL GATE OF THE STACK TRACE ]
    | () () |     "HALT, MORTAL DEVELOPER!
     \  ^  /       You seek the cure to your IndexError plight?
      |||||        First pay the mental toll, or wander in darkness!"
      |||||

I have already prepared a bounds-checked solution.
The riddle is optional; request the direct answer at any time:

"I consume all characters from dusk till dawn, ignoring your boundaries 
until the very last quotation mark. What regex quantifier am I?"

Choose wisely:
  [A] Greedy quantifier (e.g., `.*`)
  [B] Lazy quantifier (e.g., `.*?`)
  [C] Possessive quantifier (e.g., `.*+`)

Reply with your answer for the game, or type `!skip` to receive the code now.
```

---

## 🎲 Looking for Pure Tabletop D&D?

Did your real-world gaming group cancel game night again? Check out our dedicated standalone D&D repository:  
👉 **[DnD-Agents (`dnd-agents`)](https://github.com/c4da/dnd-agents)**
- **`classic-dnd-dungeon-master`**: 1980s Gary Gygax style DM with roguelike ASCII dungeon maps, d20 checks, and monster tables.
- **`dnd-party-of-agents`**: Asks one compatible agent to portray a four-member AI party (Paladin, Barbarian, Rogue, Wizard).
- **`dnd-quest-the-lost-shrine`**: Turnkey starter adventure module (*The Lost Shrine of the Sun-Stone*).

---

## 🛡️ Need Actual Enterprise Safety?

If your boss is watching or you need serious agent guardrails, check out our companion project:  
👉 **[AgentTrace Skills (`agent-trace-skills`)](https://github.com/c4da/agent-trace-skills)**
- `agent-runtime-firewall`: Pre-flight command safety, DLP secret redaction & Pre-Image CAS rollback.
- `local-model-offload`: Zero-token local offload to Ollama / PC-2 nodes.
- `agent-decision-ledger`: Cryptographic SHA-256 milestone ledger.
- `multi-agent-conflict-coordinator`: Split-brain concurrency leases.

---

## Safety and Limitations

- These are prompt-only presentation layers, not autonomous workers or a
  security product.
- The RPG and riddle modes are optional and must never withhold urgent,
  security, production, or explicitly requested help.
- Persona voice must not alter code syntax, hide uncertainty, or replace tests
  and evidence.
- The cyberpunk mode is limited to authorized defensive analysis and does not
  provide credential theft, spoofing, persistence, or unauthorized access
  instructions.

## 🛠️ Validation & Integrity

Every skill includes an official `manifest.json` and cryptographically verifiable `SKILL.md`:
```bash
python tools/validate_catalog.py
python tools/validate_catalog.py --check
python -m unittest discover -s tools -p "test_*.py"
```

---

## 📄 License
MIT for original repository material. See [NOTICE.md](NOTICE.md) for
third-party references and marketplace redistribution guidance.
