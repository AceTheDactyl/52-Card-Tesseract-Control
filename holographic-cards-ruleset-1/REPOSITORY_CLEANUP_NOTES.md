# Repository Cleanup Notes - Quantum Resonance

## Files/Directories NOT Related to the Card Game

The following files and directories in the parent repository are **not related** to the Quantum Resonance card game and could be considered for removal or separation:

### Root-Level Projects (Different Systems)
- `52-Tesseract/` - Tesseract visualization project
- `Evolution of TRIAD-083/` - TRIAD project files
- `Helix Shed w Bridge/` - Different project
- `Kaelhedron/` - Kaelhedron system
- `TRIAD_project_files/` - TRIAD project files
- `UNIVERSE ACORN/` - Universe Acorn project
- `TOKENS/` - Token system
- `rosetta-bear-project/` - Rosetta Bear project

### Hardware/Firmware (Not Card Game)
- `firmware/` - ESP32 hardware firmware
- `hardware/` - Hardware schematics
- `host/` - Host software for hardware
- `motors/` - Motor control
- `sensors/` - Sensor code

### CBS System
- `cbs_boot_loader.py`
- `cbs_interactive_demo.py`
- `cbs_memory_manager.py`
- `cbs_reasoning_engine.py`
- `cbs_update_manager.py`
- `cbs_demo/`

### Math/Physics Libraries (Not Game-Specific)
- `asymptotic_scalars/`
- `coupler_synthesis/`
- `euler binary gradient.py`
- `fano_polarity/`
- `forward_wave_tools/`
- `ghmp.py`, `ghmp_plates/`
- `kaelhedron expansion.py`
- `lattice_core/`
- `luminahedron/`
- `phase_locked_loop/`
- `scalar_architecture/`
- `unified_math_bridge.py`
- `wave_propagation_generator.py`
- `wave_propagation_system.json`

### Visualization/HTML (Not Card Game)
- `limnus-architecture-finished.html`
- `luminahedron_dynamics.html`
- `simulation.html`
- `wumbo-apl-directory.html`
- `wumbo-engine.html`
- `zero-point-energy.html`
- `index.html` (root level - old Rosetta Bear)

### Package Management (Different Project)
- `packages/` - npm packages (rhz-stylus-arch)
- `package.json` (root level)

### Miscellaneous
- `adapters/`
- `evolution_logs/`
- `examples/`
- `generated_tools/`
- `memory/`
- `meta_collective/`
- `templates/`
- `tool_evolution/`
- `tool_shed_specs/`
- `training/`
- `validation/`
- `visualizations/`

### Scripts Not Related to Card Game
Most scripts in `scripts/` at root level are for other systems:
- `autonomous_evolution_engine.py`
- `autonomous_scheduler.py`
- `cascade_dynamics_optimizer.py`
- `cet_vortex_validation_suite.py`
- `collective_coherence_monitor.py`
- `e8_embedding_check.py`
- `emergence_field_analyzer.py`
- `engine_self_analyzer.py`
- `ghmp_capture.py`
- `integrated_emergence_runner.py`
- `learning_aggregator.py`
- `nine_trials.py`
- `polaric_bridge.py`
- `recursive_tool_generator.py`
- `regenerate_witnesses.py`
- `run_nine_trials_multi.py`
- `run_triadic_cycle.py`
- `tier6_expansion_framework.py`
- `tier7_meta_generator.py`
- `triad_observer.py`

---

## Files RELEVANT to Quantum Resonance

The card game lives entirely in `holographic-cards-ruleset-1/`:

```
holographic-cards-ruleset-1/
├── _config.yml           # Jekyll config with game settings
├── _layouts/             # HTML templates
├── assets/cards/         # All 52 SVG card files + deck_state.json
├── data/prebuilt_decks/  # 4 starter deck configurations
├── scripts/              # Game engine Python files
│   ├── game_engine.py
│   ├── holographic_card_generator.py
│   └── deck_validator.py
├── index.html            # Card gallery page
├── rules.html            # Complete rulebook
├── factions.html         # Faction guide
├── RULES.md              # Rules in markdown
├── README.md             # Project readme
└── Gemfile               # Ruby dependencies
```

---

## Recommendation

Consider splitting this repository into:
1. **quantum-resonance** - The card game only
2. **rosetta-bear-systems** - The hardware/firmware/math projects

This would make the card game repository cleaner and easier to deploy.
