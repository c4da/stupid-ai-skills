# 🤡 Stupid AI Skills (`#ai-skills`)

> **Hilarious, Dramatic & Questionably Useful Personas for AI Coding Agents**  
> Because life is too short to let your AI speak like a polite junior enterprise consultant.  
> Compatible with **Claude Code**, **Cursor**, **Windsurf**, **Antigravity**, **GitHub Copilot CLI**, and **Hermes**.

[![GitHub Topics](https://img.shields.io/badge/topic-%23ai--skills-blue.svg)](https://github.com/topics/ai-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![SkillsMP Indexed](https://img.shields.io/badge/Indexed-SkillsMP-success.svg)](https://skillsmp.com)
[![Enterprise Counterpart](https://img.shields.io/badge/Looking%20for%20serious%20security%3F-agent--trace--skills-red.svg)](https://github.com/c4da/agent-trace-skills)

---

## ❓ Proč to proboha vzniklo? (Why Does This Exist?)

Everyone is out there building autonomous enterprise agents, multi-agent RAG pipelines, and compliant corporate guardrails. We build those too ([see our serious sister repo `agent-trace-skills`](https://github.com/c4da/agent-trace-skills)).

**But at 11 PM on a Friday**, we realized what the software industry *actually* needed wasn't another polite agent asking:  
*"I noticed you have a potential NullPointerException, would you like me to suggest a refactor?"*

What we needed was a **Warhammer 40,000 Tech-Priest** to violently berate us for our decaying biological weakness and cleanse our heretical unwrap calls with sacred binary unguents. 

And if that doesn't fit your vibe, you can have **Jedi Master Yoda** teach your borrow checker in inverted OSV syntax, or a **Drunken Pirate Captain** treat your git conflicts like a Kraken attack.

---

## ⚡ 1-Line Quick Install

### Claude Code
```bash
# Add any skill directly to Claude Code
npx @agensi/skills add talk-like-tech-priest
```

### Antigravity & Agent Environments
```bash
git clone https://github.com/c4da/stupid-ai-skills.git
cp -r stupid-ai-skills/skills/talk-like-tech-priest ~/.gemini/antigravity/skills/
```

### Cursor & Windsurf
Simply copy the contents of `SKILL.md` into your `.cursorrules` or `.windsurfrules` file.

---

## 🎭 The Hall of Questionable Skills & Games

### 🕹️ Terminal Games & Hostage Takers
| Skill | Type | Description |
| :--- | :--- | :--- |
| **[`terminal-riddle-tollgate`](skills/terminal-riddle-tollgate)** | Mini-Game | **Holds your bug fix hostage.** You cannot have the working code until you solve Barnaby the Byte-Troll's CS riddle or logic puzzle! |
| **[`ascii-rpg-boss-fight`](skills/ascii-rpg-boss-fight)** | Turn-Based RPG | **Converts errors into retro dungeon boss fights.** The bug is an ASCII monster (NullPointer Wyrm, Concurrency Hydra); you must choose combat actions (`Cast std::sync::Mutex`, `Drink Espresso`) to slay it and reveal the patch! |

### 🎙️ Outrageous Personas
| Skill | Persona | Flavour Quote |
| :--- | :--- | :--- |
| **[`talk-like-tech-priest`](skills/talk-like-tech-priest)** | Warhammer 40K Adeptus Mechanicus | *"[VOX-STATIC] Silence, fragile meat-vessel! Your crude biological neurons offend the Omnissiah with this 1,500-line monolithic abominable mass."* |
| **[`talk-like-yoda`](skills/talk-like-yoda)** | Jedi Grand Master (OSV syntax) | *"Strong with the borrow checker, your code must be. Careless with `.clone()` you have been; lead to suffering, excessive allocations will."* |
| **[`talk-like-pirate`](skills/talk-like-pirate)** | 17th Century Swashbuckler Captain | *"Ahoy, ye scurvy dog! Batten down the hatches, a three-way git merge conflict Kraken approaches off the port bow! Swab the diff deck!"* |
| **[`cyberpunk-netrunner`](skills/cyberpunk-netrunner)** | Night City / Neuromancer Netrunner | *"Neural jacks engaged. Military-grade Black ICE detected in your unauthenticated route. Flatline that endpoint before Arasaka traces the ping."* |

---

## 🍿 Live Demos (Show, Don't Tell)

### Demo 1: Asking the Tech-Priest to review a sloppy Python script

```text
User: Can you fix my script? It crashes sometimes with IndexError.

Agent (Tech-Priest):
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

Praise be the Omnissiah! Repent of your biological carelessness.
```

---

### Demo 2: Yoda debugging a Rust lifetime issue

```text
User: Why is Rust yelling at me about borrowed values living longer than the scope?

Agent (Yoda):
Hmm. Great impatience in you, I sense.
Outlived by the reference, the owned value is.
To reference data that exists no longer, a dangerous path that is.
Lead to dangling pointers it does. To the Dark Side of segmentation faults, that way lies.

Lifetimes must you align, yes:
fn harvest_wisdom<'a>(scroll: &'a str) -> &'a str {
    // Kept alive the reference remains, as long as the scroll exists, hmm!
    scroll.trim()
}

Patience you must have. With the compiler fight you do not; learn from it, you must!
```

### Demo 3: The Toll Troll holding a bug fix hostage

```text
User: How do I fix this IndexError in my Python script?

Agent (Byte-Troll):
       ___
     /     \      [ TOLL GATE OF THE STACK TRACE ]
    | () () |     "HALT, MORTAL DEVELOPER!
     \  ^  /       You seek the cure to your IndexError plight?
      |||||        First pay the mental toll, or wander in darkness!"
      |||||

I have already crafted your immaculate, bounds-checked solution. 
BUT NONE SHALL PASS without answering this riddle:

"I consume all characters from dusk till dawn, ignoring your boundaries 
until the very last quotation mark. What regex quantifier am I?"

Choose wisely:
  [A] Greedy quantifier (e.g., `.*`)
  [B] Lazy quantifier (e.g., `.*?`)
  [C] Possessive quantifier (e.g., `.*+`)

Reply with your answer to unlock the code! (Or type `!skip` if you're a coward).
```

---

## 🛠️ Validation & Integrity

Every skill includes an official `manifest.json` and cryptographically verifiable `SKILL.md`:
```bash
python tools/validate_catalog.py
```

---

## 🛡️ Need Actual Enterprise Safety?

If your boss is watching or you need serious agent guardrails, check out our companion project:
👉 **[AgentTrace Skills (`agent-trace-skills`)](https://github.com/c4da/agent-trace-skills)**
- `agent-runtime-firewall`: Pre-flight command safety, DLP secret redaction & Pre-Image CAS rollback.
- `local-model-offload`: Zero-token local offload to Ollama / PC-2 nodes.
- `agent-decision-ledger`: Cryptographic SHA-256 milestone ledger.
- `multi-agent-conflict-coordinator`: Split-brain concurrency leases.

---

## 📄 License
MIT. Go wild, fork it, and teach your AI some attitude.
