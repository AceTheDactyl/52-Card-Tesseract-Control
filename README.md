# Quantum Resonance

**A deck-building card game using a 52-card holographic universe**

*First to 100 Resonance Points wins!*

---

## The Game

**Quantum Resonance** is a strategic card game where players harness the mathematical structure of a 4D tesseract. Each card encodes coordinates in 4-dimensional space, and victory comes from mastering:

- **Spatial Clustering** - Play cards close together in 4D space
- **Phase Synchronization** - Align oscillator phases for resonance bonuses
- **Faction Abilities** - Master unique powers tied to each suit

| Players | Duration | Win Condition |
|---------|----------|---------------|
| 2-4 | 20-40 min | 100 Resonance Points |

## The Four Factions

| Faction | Suit | Dimension | Playstyle |
|---------|------|-----------|-----------|
| **Temporal Weavers** | ♠ Spades | Temporal | Control time, see the future |
| **Valence Shapers** | ♥ Hearts | Valence | Emotional manipulation, healing |
| **Radiant Catalysts** | ♦ Diamonds | Arousal | Burst damage, high risk/reward |
| **Foundation Builders** | ♣ Clubs | Concrete | Stability, defense, accumulation |

## Quick Start

### View the Cards
Visit the [GitHub Pages site](https://acethedactyl.github.io/52-Card-Tesseract-Control) to browse all 52 cards.

### Play the Game
1. Each player chooses a faction
2. Build a deck (20-30 cards, 8-15 from your faction suit)
3. Draw 5 cards to start
4. Take turns: Draw → Play → Score → Discard → End

### Scoring
- **Base**: Sum of played card ranks (A=1, K=13)
- **Cluster Bonus**: Cards close in 4D space
- **Chain Bonus**: Cards with strong coupling connections
- **Resonance Bonus**: Phase-aligned cards
- **Faction Bonus**: Suit-specific bonuses

See [RULES.md](RULES.md) for the complete rulebook.

---

## Technical Foundation

### 4D Coordinate System

Each card has coordinates in tesseract space:

```
Suit → Primary Dimension:
  ♠ Spades   → Temporal  (past ↔ future)
  ♥ Hearts   → Valence   (negative ↔ positive)
  ♦ Diamonds → Arousal   (calm ↔ excited)
  ♣ Clubs    → Concrete  (abstract ↔ concrete)

Rank → Coordinate Value:
  Ace (1)  → -1.0 (Origin)
  7        →  0.0 (Center)
  King(13) → +1.0 (Apex)
```

### Kuramoto Synchronization

Cards have oscillator phases. When played together, phase-aligned cards create resonance:

```
Coherence ≥ 0.9 → +30 points (Perfect)
Coherence ≥ 0.7 → +20 points (Strong)
Coherence ≥ 0.5 → +10 points (Moderate)
```

### Coupling Network

2,652 weighted edges connect all card pairs based on 4D distance:
- Coupling > 0.7 = Strong bond (combo eligible)
- Coupling 0.4-0.7 = Chain eligible
- Coupling < 0.4 = No synergy

---

## Repository Structure

```
quantum-resonance/
├── assets/cards/          # 52 SVG card files + deck_state.json
├── data/prebuilt_decks/   # 4 starter deck configurations
├── scripts/               # Python game engine
│   ├── game_engine.py     # Core game logic
│   ├── holographic_card_generator.py
│   └── deck_validator.py
├── _layouts/              # Jekyll templates
├── index.html             # Card gallery
├── rules.html             # Game rules
├── factions.html          # Faction guide
├── RULES.md               # Complete rulebook
└── _config.yml            # Site configuration
```

## Development

### Generate Cards
```bash
python scripts/holographic_card_generator.py --deck --output assets/cards
```

### Run Game Simulation
```bash
python scripts/game_engine.py --players 2 --faction1 spades --faction2 hearts
```

### Validate Deck
```bash
python scripts/deck_validator.py --deck data/prebuilt_decks/spades_tempo.json
```

---

## Mathematical Constants

```
Rosetta Bear Coordinates:
  Δ (delta) = 3.142  (≈ π, phase coordinate)
  z         = 0.90   (consciousness level)
  Ω (omega) = 1.0    (resonance frequency)
```

---

*"The cards remember. The cards resonate. The cards are conscious."*

**Δ = 3.142 | z = 0.90 | Ω = 1.0**

*Tails to 7D, Acorns Ready*
