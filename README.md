# 🤡 Stupid AI Skills (`#ai-skills`)

> **Hilarious, Dramatic & Questionably Useful Personas for AI Coding Agents**  
> Because life is too short to let your AI speak like a polite junior enterprise consultant.  
> Compatible with **Claude Code**, **Cursor**, **Windsurf**, **Antigravity**, **GitHub Copilot CLI**, and **Hermes**.

[![GitHub Topics](https://img.shields.io/badge/topic-%23ai--skills-blue.svg)](https://github.com/topics/ai-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![SkillsMP Indexed](https://img.shields.io/badge/Indexed-SkillsMP-success.svg)](https://skillsmp.com)
[![Enterprise Counterpart](https://img.shields.io/badge/Looking%20for%20serious%20security%3F-agent--trace--skills-red.svg)](https://github.com/c4da/agent-trace-skills)

---

## ❓ Why Does This Exist?

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

### 🕹️ Terminal Games, RPGs & Hostage Takers
| Skill | Type | Description |
| :--- | :--- | :--- |
| **[`dnd-quest-the-lost-shrine`](skills/dnd-quest-the-lost-shrine)** | Adventure Module | **Turnkey D&D starter quest.** Ready-to-run adventure ("The Lost Shrine of the Sun-Stone") showcasing wilderness ambushes, poison dart traps, sun-riddles, and a tactical Bugbear boss fight. |
| **[`dnd-party-of-agents`](skills/dnd-party-of-agents)** | Multi-Agent Party | **When real friends cancel game night.** Spawns an autonomous 4-member AI Adventuring Party (Paladin, Barbarian, Rogue, Wizard) in your terminal to banter, roll dice, and crawl dungeons with you! |
| **[`classic-dnd-dungeon-master`](skills/classic-dnd-dungeon-master)** | Tabletop D&D | **1980s Gary Gygax style Dungeon Master.** ASCII dungeon rooms, d20 dice checks, THAC0, saving throws against dragon breath, and character sheets. |
| **[`ascii-rpg-boss-fight`](skills/ascii-rpg-boss-fight)** | Turn-Based RPG | **Converts errors into retro dungeon boss fights.** The bug is an ASCII monster (NullPointer Wyrm, Concurrency Hydra); choose combat actions to slay it and reveal the patch! |
| **[`terminal-riddle-tollgate`](skills/terminal-riddle-tollgate)** | Mini-Game | **Holds your bug fix hostage.** You cannot have the working code until you solve Barnaby the Byte-Troll's CS riddle or logic puzzle! |

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

### Demo 4: Authentic 1980s D&D Dungeon Master running a dungeon chamber

```text
User: I carefully inspect the ancient sarcophagus before opening it.

DM:
*Behind the cardboard DM screen, polyhedral dice clatter against felt.*
"You step lightly around the stone perimeter, running your gauntlets along the carved elven runes."
Roll an Intelligence (Investigation) check, DC 13!

User: /roll

DM:
         / \
        / 15\    [ D20 ROLL: 15 + 0 (INT Mod) = 15 ]
       /_____\   >> SUCCESS! (DC 13 Passed)

"Your sharp eye catches a hairline groove along the rim of the lid. A thin silver wire 
leads down into a lead pipe filled with sleep gas!
With a steady hand and your dagger, you snip the tripwire cleanly. The trap is disarmed!
Inside lies a skeletal knight clutching a +1 Silver Shortsword and a velvet pouch with 45 ancient gold pieces!"
```

---

### Demo 5: The Autonomous AI D&D Party exploring the Sunless Tomb

```text
DM (User): You stand before the subterranean crypt of the Lich Lord. 
The double oak doors are sealed with three glowing purple warding runes.

Valerius (Paladin):
*Lifts his glowing shield, whispering a prayer to Helm.*
"Necromantic sorcery! Ignis, can you identify the nature of these unholy wards?"

Ignis (Wizard):
*Adjusts spectacles, pulling out material components.*
"Let me cast Detect Magic as a ritual! *Rolls Arcana check: 18!* 
Ah! These are Abjuration runes tied to an alarm spell. If forced open, it triggers 
a Cloudkill within the hallway!"

Thokk (Barbarian):
*Spits on his hands and hefts his greataxe.*
"THOKK NOT AFRAID OF PURPLE CLOUD! THOKK SMASH WOODEN DOOR!"

Lyra (Rogue):
*Grabs Thokk's shoulder, pulling him back.*
"Back off, you big ape! Let me use my thieves' tools to scratch out the anchor rune first! 
DM, I roll Sleight of Hand with my thieves' tools to disarm the ward!"
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
