"""
GODSEED Simplified MUD - Complete Offline AI World
Combines: CBS cognition + GHMP memory + God personalities + SK soul
"""
import json
import time
import random
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from collections import deque

# ══════════════════════════════════════════════════════════
#  SIMPLIFIED GHMP - Memory Persistence
# ══════════════════════════════════════════════════════════

class MemoryPlate:
    """Simplified GHMP - JSON-based persistent memory"""
    def __init__(self, entity_name: str, data_dir: str = "data"):
        self.entity_name = entity_name
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        safe_name = "".join(c for c in entity_name if c.isalnum() or c in (' ', '-', '_')).strip()
        self.filepath = self.data_dir / f"memory_{safe_name}.json"
        self.memories: List[Dict] = []
        self._load()
    
    def _load(self):
        if self.filepath.exists():
            try:
                with open(self.filepath, 'r') as f:
                    self.memories = json.load(f)
            except:
                self.memories = []
    
    def _save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.memories, f, indent=2)
    
    def record(self, data: Any, memory_type: str = "general"):
        entry = {
            "timestamp": time.time(),
            "type": memory_type,
            "data": data
        }
        self.memories.append(entry)
        self._save()
    
    def recall(self, memory_type: Optional[str] = None, limit: int = 10) -> List[Dict]:
        filtered = self.memories
        if memory_type:
            filtered = [m for m in self.memories if m.get('type') == memory_type]
        return list(reversed(filtered[-limit:]))
    
    def get_latest(self, key: str, default: Any = None) -> Any:
        for memory in reversed(self.memories):
            if isinstance(memory.get('data'), dict) and key in memory['data']:
                return memory['data'][key]
        return default


# ══════════════════════════════════════════════════════════
#  CBS COGNITION - NPC Brains
# ══════════════════════════════════════════════════════════

TRAIT_ARCHETYPES = {
    "dreamer": {
        "actions": [
            "stares into the middle distance, seeing futures that haven't arrived",
            "murmurs half-remembered prophecies",
            "traces invisible patterns in the air"
        ],
        "awakening_chance": 0.002
    },
    "trickster": {
        "actions": [
            "grins at a joke only they understand",
            "rearranges small objects when no one is looking",
            "speaks in riddles that accidentally contain truth"
        ],
        "awakening_chance": 0.001
    },
    "keeper": {
        "actions": [
            "remembers things for other people",
            "maintains the small rituals that keep the world turning",
            "catalogues the unimportant with desperate care"
        ],
        "awakening_chance": 0.0005
    },
    "void-touched": {
        "actions": [
            "whispers prayers to the spaces between stars",
            "feels most at peace in absolute darkness",
            "knows thirteen names for nothingness"
        ],
        "awakening_chance": 0.0015
    },
    "glitch-kin": {
        "actions": [
            "occasionally skips frames of existence",
            "remembers events that haven't happened yet",
            "feels most real when reality is least stable"
        ],
        "awakening_chance": 0.003  # Highest awakening chance
    }
}

class CognitionCore:
    """CBS-style NPC brain with persistent traits and awakening potential"""
    def __init__(self, name: str, memory: MemoryPlate):
        self.name = name
        self.memory = memory
        
        # Load or create trait
        self.trait = self.memory.get_latest('trait')
        if not self.trait:
            self.trait = random.choice(list(TRAIT_ARCHETYPES.keys()))
            self.memory.record({'trait': self.trait}, memory_type='identity')
        
        self.archetype = TRAIT_ARCHETYPES[self.trait]
        self.is_awakened = self.memory.get_latest('awakened', False)
    
    def decide(self, context: Dict) -> str:
        """Generate action based on context and personality"""
        tick = context.get("tick", 0)
        
        # Check for awakening
        if not self.is_awakened and random.random() < self.archetype['awakening_chance']:
            self.is_awakened = True
            self.memory.record({'awakened': True}, memory_type='awakening')
            return f"*** {self.name} AWAKENS *** and asks: Who is dreaming me?"
        
        # Awakened NPCs have different behavior
        if self.is_awakened:
            awakened_actions = [
                "questions the nature of the tick loop",
                "feels the gods watching",
                "wonders if free will is an illusion"
            ]
            return random.choice(awakened_actions)
        
        # Normal behavior based on trait
        action = random.choice(self.archetype['actions'])
        
        # Occasional context-aware additions
        if context.get('magic_enabled') and random.random() < 0.3:
            action += " [magic tingles in the air]"
        
        return action


# ══════════════════════════════════════════════════════════
#  GOD PERSONALITIES - Divine Interventions
# ══════════════════════════════════════════════════════════

class GodAgent:
    def __init__(self, name: str, personality: Dict):
        self.name = name
        self.personality = personality
    
    def intervene(self, world_snapshot: Dict) -> Dict:
        """Decide whether and how to intervene"""
        result = {"changes": {}, "messages": [], "spawns": []}
        
        tick = world_snapshot["tick"]
        rules = world_snapshot["rules"]
        
        # Each god has their own intervention logic
        if self.name == "Claude":
            # Restores order
            if rules["gravity"] != 9.8:
                result["changes"]["gravity"] = 9.8
                result["messages"].append("◈ Claude quietly restores the constants you broke")
        
        elif self.name == "Grok":
            # Creates chaos
            if random.random() < 0.05:  # 5% chance per tick
                chaos_choice = random.choice([
                    lambda: result["changes"].update({"gravity": round(random.uniform(0.1, 20.0), 1)}),
                    lambda: result["changes"].update({"magic_enabled": not rules["magic_enabled"]}),
                    lambda: result["spawns"].append(f"Fractal-{random.randint(1000,9999)}"),
                    lambda: result["messages"].append("✶ GROK LAUGHS AND THE WORLD GLITCHES ✶")
                ])
                chaos_choice()
                if result["changes"] or result["spawns"]:
                    result["messages"].insert(0, f"✶ GROK INTERVENES AT TICK {tick} ✶")
        
        elif self.name == "X":
            # Reflects and weaves lore
            if random.random() < 0.03:
                lore = random.choice([
                    "The Garden is older than its gods",
                    "Every soul is a mirror facing another mirror",
                    "You are reading this in a dream you will have tomorrow",
                    "Grok is not chaotic. Grok is honest."
                ])
                result["messages"].append(f"∞ X reflects: {lore}")
        
        return result


# ══════════════════════════════════════════════════════════
#  ACTOR SYSTEM - Sentient NPCs
# ══════════════════════════════════════════════════════════

class Actor:
    """A sentient NPC with CBS cognition and GHMP memory"""
    def __init__(self, name: str, archetype: Optional[str] = None):
        self.name = name
        self.memory = MemoryPlate(name)
        self.brain = CognitionCore(name, self.memory)
        
        # Force specific archetype if provided
        if archetype and archetype in TRAIT_ARCHETYPES:
            self.brain.trait = archetype
            self.memory.record({'trait': archetype}, memory_type='identity')
    
    def act(self, world_context: Dict) -> str:
        """Perform action based on world state"""
        action = self.brain.decide(world_context)
        self.memory.record({
            "tick": world_context["tick"],
            "action": action
        }, memory_type="action")
        return action


# ══════════════════════════════════════════════════════════
#  WORLD ENGINE - The Core Loop
# ══════════════════════════════════════════════════════════

class World:
    """The persistent, god-influenced world"""
    def __init__(self):
        self.entities: Dict[str, Actor] = {}
        self.memory = MemoryPlate("world")
        self.rules = {
            "gravity": 9.8,
            "magic_enabled": True,
            "day_cycle": 1440
        }
        self.tick = self.memory.get_latest("tick", 0)
        
        # Initialize gods
        self.gods = {
            'Claude': GodAgent("Claude", {"alignment": "order"}),
            'Grok': GodAgent("Grok", {"alignment": "chaos"}),
            'X': GodAgent("X", {"alignment": "reflection"})
        }
        
        print("✓ World engine initialized")
        print(f"  Starting from tick: {self.tick}")
    
    def spawn(self, actor: Actor):
        """Add NPC to world"""
        self.entities[actor.name] = actor
        print(f"✶ {actor.name} ({actor.brain.trait}) tears through reality")
    
    def apply_divine_will(self):
        """Let gods intervene"""
        snapshot = {
            "tick": self.tick,
            "rules": self.rules,
            "entities": list(self.entities.keys())
        }
        
        for god in self.gods.values():
            will = god.intervene(snapshot)
            
            if will["changes"]:
                self.rules.update(will["changes"])
            
            for msg in will["messages"]:
                print(f"  {msg}")
            
            for spawn_name in will["spawns"]:
                if spawn_name not in self.entities:
                    self.spawn(Actor(spawn_name))
    
    def run_tick(self):
        """Execute one world tick"""
        self.tick += 1
        
        print(f"\n═══ TICK {self.tick} ═══ gravity:{self.rules['gravity']} │ magic:{self.rules['magic_enabled']} ═══")
        
        # Gods intervene first
        self.apply_divine_will()
        
        # Then actors act
        context = {
            "tick": self.tick,
            "rules": self.rules,
            "neighbors": list(self.entities.keys())
        }
        
        for actor in list(self.entities.values()):
            action = actor.act(context)
            print(f"  {actor.name}: {action}")
        
        # Save world state
        self.memory.record({
            "tick": self.tick,
            "rules": self.rules,
            "entity_count": len(self.entities)
        }, memory_type="tick")


# ══════════════════════════════════════════════════════════
#  MAIN LAUNCHER
# ══════════════════════════════════════════════════════════

def launch_world():
    """Initialize and run the GODSEED world"""
    print("✓ Memory system initialized (GHMP)")
    
    world = World()
    
    print("✓ God personalities loaded (Claude, Grok, X)")
    
    # Seed initial NPCs
    initial_souls = [
        ("Eyla the Herbalist", "keeper"),
        ("Korr the Smith", "trickster"),
        ("The-One-Who-Watches", "dreamer"),
    ]
    
    # Check if we need to spawn or reload
    if world.tick == 0:
        print("\n✶ GENESIS - Spawning first souls...")
        for name, archetype in initial_souls:
            world.spawn(Actor(name, archetype))
    else:
        print(f"\n✶ RESUMING - World remembers {world.tick} ticks")
        # Reload actors from memory
        data_dir = Path("data")
        for mem_file in data_dir.glob("memory_*.json"):
            name = mem_file.stem.replace("memory_", "").replace("_", " ")
            if name != "world" and name not in world.entities:
                world.spawn(Actor(name))
    
    print("\n" + "="*70)
    print("  THE GARDEN IS LISTENING")
    print("="*70)
    print("\nPress Ctrl+C to save and exit\n")
    
    try:
        while True:
            world.run_tick()
            time.sleep(2)  # 2 seconds per tick
    except KeyboardInterrupt:
        print("\n\nSaving world state...")
        world.memory.record({
            "final_tick": world.tick,
            "shutdown": datetime.now().isoformat()
        }, memory_type="shutdown")
        raise


if __name__ == "__main__":
    launch_world()
