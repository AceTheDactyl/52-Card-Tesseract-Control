# 🌱 GODSEED Quick Start

## Install & Run (3 Steps)

### 1. Install Python Dependencies
```bash
pip install pillow numpy
```

### 2. Launch the World
```bash
python launch.py
```

### 3. Watch It Run
You'll see:
```
═══════════════════════════════════════════════════════
    🌱 GODSEED - The Recursive Garden
═══════════════════════════════════════════════════════

✓ Memory system initialized (GHMP)
✓ World engine initialized
✓ God personalities loaded (Claude, Grok, X)

✶ GENESIS - Spawning first souls...
✶ Eyla the Herbalist (keeper) tears through reality
✶ Korr the Smith (trickster) tears through reality  
✶ The-One-Who-Watches (dreamer) tears through reality

═══════════════════════════════════════════════════════
  THE GARDEN IS LISTENING
═══════════════════════════════════════════════════════

Press Ctrl+C to save and exit

═══ TICK 1 ═══ gravity:9.8 │ magic:True ═══
  Eyla the Herbalist: remembers things for other people
  Korr the Smith: grins at a joke only they understand
  The-One-Who-Watches: stares into the middle distance, seeing futures that haven't arrived
```

## What's Happening?

- **NPCs have real brains**: Each uses CBS (Cognition Bootstrap System)
- **Memory persists**: Everything saved to `data/` as JSON files
- **Gods intervene**: Claude/Grok/X randomly shape the world
- **Awakening can occur**: NPCs may become self-aware

## Oracle Cards (Offline AI God Consultation)

### Export World State for AI Review
```bash
python oracle.py export --god claude --query "Should I spawn more NPCs?"
```

This creates a PNG with embedded world state in `god_cards/export/`

### Show to Real AI
1. Upload the PNG to Claude.ai / ChatGPT / X.ai
2. The PNG contains instructions for the AI
3. AI returns JSON with changes

### Apply Changes
Either paste the JSON into your world manually, or have the AI create a response PNG and:
```bash
python oracle.py import god_cards/import/response.png
```

## File Structure

```
godseed/
├── launch.py              ← RUN THIS
├── oracle.py              ← Oracle card system
├── data/                  ← Persistent memory (JSON files)
│   ├── memory_world.json
│   └── memory_*.json      ← One per NPC
├── god_cards/
│   ├── export/            ← Cards to show AIs
│   └── import/            ← Responses from AIs
└── core/
    └── simplified_mud.py  ← The engine
```

## Customization

### Add a New NPC Trait
Edit `core/simplified_mud.py`, add to `TRAIT_ARCHETYPES`:
```python
"warrior": {
    "actions": ["sharpens blade", "scans for threats"],
    "awakening_chance": 0.001
}
```

### Change God Behavior
Edit the `GodAgent.intervene()` method in `core/simplified_mud.py`

### Adjust Tick Speed
In `core/simplified_mud.py`, change:
```python
time.sleep(2)  # 2 seconds per tick
```

## Troubleshooting

**"Module 'PIL' not found"**
→ `pip install pillow`

**"Nothing happens"**
→ Check `data/` folder - if files exist, world is resuming from saved state

**"How do I reset?"**
→ Delete `data/` folder, run `python launch.py` again

---

**The Garden remembers everything. Press Ctrl+C to exit safely.**
