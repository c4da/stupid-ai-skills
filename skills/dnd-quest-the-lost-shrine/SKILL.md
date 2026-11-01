---
name: dnd-quest-the-lost-shrine
description: A complete, ready-to-run D&D starter adventure module ("The Lost Shrine of the Sun-Stone"). Plugs into classic-dnd-dungeon-master or dnd-party-of-agents to showcase all core tabletop mechanics—stealth, perception, trap disarming, riddles, tactical turn-based boss combat, and loot.
license: MIT
compatibility: Compatible with classic-dnd-dungeon-master, dnd-party-of-agents, and all AI agents (Claude Code, Cursor, Windsurf, Antigravity, Copilot CLI, Hermes, ChatGPT).
metadata:
  author: c4da
  version: "1.0.0"
  categories: ["fun", "game", "dnd", "quest-module", "adventure", "tabletop"]
  tags: ["dnd", "quest", "adventure-module", "dungeon-crawler", "starter-quest", "tabletop", "ascii-maps"]
---

# ⚔️ D&D Adventure Module: The Lost Shrine of the Sun-Stone (`dnd-quest-the-lost-shrine`)

> *"The village elder grips your arm with trembling hands: 'The goblins stole the Sun-Stone from our altar under cover of storm! Without its golden light, our crops will wither and the shadow beasts of the crags will descend upon us. Recover the stone from their sunken shrine, brave adventurers, and glory shall be yours!' "*

This skill provides a **complete, turnkey D&D quest module** designed to showcase and guide players through all core tabletop Dungeons & Dragons mechanics.

---

## 🔌 How This Module Plugs In

This quest can be run in two ways:
1. **Solo / Group with DM (`classic-dnd-dungeon-master`)**:  
   The agent acts as the DM, narrating this exact module, rolling monster dice, and presenting the tactical ASCII maps to the player(s).
2. **With the Autonomous AI Party (`dnd-party-of-agents`)**:  
   Sir Valerius, Thokk, Lyra, and Ignis accompany the user as full companions, debating choices and rolling for initiative throughout each chapter of the quest.

---

## 📜 Adventure Synopsis

- **Target Level**: Level 1–3 party.
- **Estimated Play Time**: 15–30 minutes in chat.
- **Setting**: The Whispering Crags, an overgrown ravine leading into an ancient buried temple.
- **Core Mechanics Showcased**:
  1. **Act I**: Wilderness tracking, Passive Perception vs. Goblin Stealth, Ranged Combat.
  2. **Act II**: Trap detection, Investigation, Thieves' Tools disarm, Riddle of the Sun.
  3. **Act III**: Full Tactical Combat, Initiative, Spells, Monster Traits, Boss Battle.
  4. **Act IV**: Looting, Magic Item identification, and Quest Resolution.

---

## 🗺️ Act I: The Overgrown Ravine (Stealth & Ambush)

### Scene Description
The party tracks muddy goblin footprints through a narrow gorge lined with thorny briars. The entrance to the ancient shrine looms ahead—a gaping maw carved into the cliffside in the shape of a screaming skull.

### ASCII Tactical Map: Act I
```text
       # # # # # # # # # # # # # # # # # # # #
       # . . . . . . . . . . . . . . . [ENTRANCE]
       # . . . . . . . . . . T T . . . . . . #   LEGEND:
       # . @ . . . . . . . . T G . . . . . . #   @ = The Party
       # . . . . . . . . . . T T . . . . . . #   G = Goblin Sentry (in bushes)
       # # # # # # # # # # # # # # # # # # # #   T = Dense Thorny Briars
```

### Mechanics Showcase:
- **Perception Check (DC 11)**: Spot the goblin scout (*Grik*) crouching behind the thorny briars with a notched shortbow.
  - *Success*: Party acts normally or attempts a surprise ranged strike.
  - *Failure*: Grik gets a Surprise Round attack (`+4 to hit, 1d6+2 piercing damage`) and screeches a warning alarm into the cave.

---

## 🗝️ Act II: Hall of the Stone Wardens (Traps & Riddles)

### Scene Description
Inside the cool stone foyer, two defaced stone statues of ancient warrior monks flank a reinforced bronze door. In the center of the flagstone floor lies a slightly raised tile connected to hidden wall apertures.

### ASCII Tactical Map: Act II
```text
       # # # # # # # # # + # # # # # # # # # #
       # . . . . . . . [DOOR] . . . . . . . . #   LEGEND:
       # . S . . . . . . . . . . . . . . S . #   S = Stone Monk Statue
       # . . . . . . . [ ^ ] . . . . . . . . #   ^ = Pressure Plate Trap
       # . . . . . . . . @ . . . . . . . . . #   @ = The Party
       # # # # # # # # # # # # # # # # # # # #
```

### Mechanics Showcase:
1. **The Poison Dart Trap (`^`)**:
   - **Investigation Check (DC 12)**: Notices the pressure plate and tiny holes drilled into the statue eyes.
   - **Thieves' Tools Check (DC 13)**: Jamming the plate with pitons or disarming the spring.
   - **Trigger / Failure**: Dexterity Saving Throw (DC 12). Failure deals `1d4 piercing + 1d6 poison damage` (half on success).
2. **The Sun-Riddle of the Bronze Door**:
   Carved in archaic Common upon the door:
   > *"I have no flesh, yet warm all land. I have no eyes, yet reveal all sand. Gaze directly upon me and you go blind; turn your back and shadow follows behind. What am I?"*
   - *Answer*: The Sun. Speaking the word causes the runes to flare with warm golden light and the door swings silently open.

---

## 👹 Act III: Sanctum of the Bugbear Chief (Boss Battle)

### Scene Description
A grand pillared sanctuary lit by sputtering torches in bronze sconces. At the far altar, resting on a pedestal, glows the golden **Sun-Stone**. Guarding it is **Kragthor**, a hulking Bugbear Chief clad in scavenged hide armor, accompanied by two reanimated skeletons.

### ASCII Tactical Map: Act III (Boss Arena)
```text
       # # # # # # # # # # # # # # # # # # # #
       # . . . . . . . [ALTAR/$] . . . . . . #   LEGEND:
       # . . . . . . . . . K . . . . . . . . #   K = Kragthor (Bugbear Chief)
       # . . P . . . . . . . . . . . . P . . #   P = Stone Pillar (Half-Cover)
       # . . Z . . . . . . . . . . . . Z . . #   Z = Skeleton Guardians (AC 13, HP 13)
       # . . . . . . . . . . . . . . . . . . #   $ = Sun-Stone on Altar
       # . . . . . . . . @ . . . . . . . . . #   @ = The Party
       # # # # # # # # # + # # # # # # # # # #
```

### Boss Stat Block: Kragthor the Bugbear
- **Armor Class**: 16 (Hide Armor, Shield)
- **Hit Points**: 27 (5d8 + 5)
- **Speed**: 30 ft
- **Attributes**: STR 15 (+2), DEX 14 (+2), CON 13 (+1), INT 8 (-1), WIS 11 (+0), CHA 9 (-1)
- **Special Trait — Brute**: Deals one extra die of damage with melee weapon attacks (included below).
- **Actions**:
  - *Morningstar*: Melee Weapon Attack, `+4 to hit, reach 5 ft. Hit: 11 (2d8 + 2) piercing damage`.
  - *Javelin*: Melee or Ranged Weapon Attack, `+4 to hit, range 30/120 ft. Hit: 9 (2d6 + 2) piercing damage`.

### Skeleton Guardians (x2)
- **Armor Class**: 13 (Armor Scraps)
- **Hit Points**: 13 (2d8 + 4)
- **Damage Vulnerability**: **Bludgeoning** (Thokk's warhammer / Valerius's mace deals DOUBLE damage!).

---

## 🏆 Act IV: The Hoard & Resolution

When Kragthor falls, his remaining minions flee in terror. The party secures the altar!

### Quest Rewards:
1. **The Sun-Stone of Pelor**:
   - Emits bright sunlight in a 20-ft radius upon command.
   - Once per dawn, can cast *Lesser Restoration* (cures disease or poison).
2. **Kragthor's Iron Treasure Chest**:
   - 65 Gold Pieces (gp), 140 Silver Pieces (sp).
   - 2 × *Potions of Healing* (heals `2d4 + 2` HP each).
   - 1 × *Scroll of Misty Step* (bonus action teleport 30 ft).
   - A silver medallion with a blue sapphire (worth 50 gp).
3. **Experience / Milestones**:
   - The party gains enough experience to reach **Level 2** (or milestones unlocked)!
   - Return to the village to receive the villagers' gratitude, a feast in the tavern, and Lord Harver's reward!
