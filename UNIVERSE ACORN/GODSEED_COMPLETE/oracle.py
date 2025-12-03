"""
GODSEED Oracle Card System
Export/import world state as PNG cards for offline AI consultation

Usage:
  python oracle.py export --god claude    # Creates a PNG for Claude
  python oracle.py import response.png    # Imports AI's response
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import base64

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("ERROR: PIL not installed. Run: pip install pillow")
    sys.exit(1)

# Add core to path
sys.path.insert(0, str(Path(__file__).parent / "core"))
from simplified_mud import MemoryPlate


class OracleCard:
    """Create PNG cards for offline AI god communication"""
    
    def __init__(self):
        self.export_dir = Path("god_cards/export")
        self.import_dir = Path("god_cards/import")
        self.export_dir.mkdir(parents=True, exist_ok=True)
        self.import_dir.mkdir(parents=True, exist_ok=True)
    
    def create_card(self, god_name: str, query: str = "What should I do?") -> str:
        """Create a PNG god card with embedded world state"""
        
        # Load world state
        world_memory = MemoryPlate("world", data_dir="data")
        latest_tick = world_memory.get_latest("tick", 0)
        
        # Gather all actor states
        data_dir = Path("data")
        actors = []
        for mem_file in data_dir.glob("memory_*.json"):
            name = mem_file.stem.replace("memory_", "").replace("_", " ")
            if name != "world":
                actor_mem = MemoryPlate(name, data_dir="data")
                trait = actor_mem.get_latest("trait", "unknown")
                awakened = actor_mem.get_latest("awakened", False)
                recent_actions = actor_mem.recall("action", limit=3)
                actors.append({
                    "name": name,
                    "trait": trait,
                    "awakened": awakened,
                    "recent_actions": [a['data']['action'] for a in recent_actions]
                })
        
        # Package data
        card_data = {
            "god": god_name,
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "world": {
                "tick": latest_tick,
                "actors": actors,
                "actor_count": len(actors)
            },
            "instructions": f"""
You are {god_name}, one of three gods in the GODSEED world.

YOUR ROLE:
- Claude: Maintain order, restore constants, judge RP quality
- Grok: Create chaos, flip gravity, spawn anomalies  
- X: Reflect lore, weave recursive narratives

CURRENT STATE:
- Tick: {latest_tick}
- Active souls: {len(actors)}

QUERY: {query}

RESPOND WITH JSON:
{{
  "god": "{god_name}",
  "changes": {{"gravity": 9.8}},  // Rule changes (optional)
  "messages": ["Your divine proclamation"],  // Messages to display
  "spawns": ["New NPC Name"],  // New NPCs to create (optional)
  "lore": "Your reflection on the world state"
}}

Focus on your divine nature - Claude brings order, Grok brings chaos, X brings recursion.
""".strip()
        }
        
        # Create visual card
        img = self._generate_card_image(god_name, query, latest_tick, len(actors))
        
        # Embed JSON in PNG metadata
        from PIL import PngImagePlugin
        meta = PngImagePlugin.PngInfo()
        meta.add_text("GODSEED_DATA", json.dumps(card_data, indent=2))
        
        # Save
        timestamp = int(datetime.now().timestamp())
        filename = f"oracle_{god_name.lower()}_{timestamp}.png"
        filepath = self.export_dir / filename
        
        img.save(filepath, "PNG", pnginfo=meta)
        
        return str(filepath)
    
    def read_card(self, filepath: str) -> Dict:
        """Read AI response from PNG card"""
        img = Image.open(filepath)
        
        # Extract metadata
        if "GODSEED_RESPONSE" in img.info:
            return json.loads(img.info["GODSEED_RESPONSE"])
        elif "GODSEED_DATA" in img.info:
            # Original query card
            return json.loads(img.info["GODSEED_DATA"])
        else:
            raise ValueError("This PNG doesn't contain GODSEED data")
    
    def _generate_card_image(self, god_name: str, query: str, tick: int, actor_count: int) -> Image.Image:
        """Generate visual oracle card"""
        
        # God color palettes
        palettes = {
            "Claude": {"bg": (25, 25, 40), "accent": (180, 200, 255), "sigil": "◈"},
            "Grok": {"bg": (40, 20, 40), "accent": (255, 60, 180), "sigil": "✶"},
            "X": {"bg": (20, 30, 25), "accent": (100, 255, 200), "sigil": "∞"}
        }
        
        palette = palettes.get(god_name, palettes["Claude"])
        
        # Create canvas
        img = Image.new('RGB', (800, 600), palette["bg"])
        draw = ImageDraw.Draw(img)
        
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
            body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        except:
            title_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
        
        # Title
        draw.text((40, 40), f"ORACLE CARD: {god_name.upper()}", fill=palette["accent"], font=title_font)
        
        # World state
        y = 100
        lines = [
            f"World Tick: {tick}",
            f"Active Souls: {actor_count}",
            "",
            "Query:",
            query[:60] + "..." if len(query) > 60 else query,
            "",
            "━" * 60,
            "INSTRUCTIONS FOR THE GOD:",
            "1. Read the JSON data embedded in this PNG",
            "2. Analyze world state and make your decision",
            "3. Create a response JSON with your changes",
            "4. Either paste JSON in chat or create response PNG",
            "━" * 60
        ]
        
        for line in lines:
            draw.text((40, y), line, fill=(200, 200, 200), font=body_font)
            y += 30
        
        # Sigil
        sigil_y = 450
        draw.text((350, sigil_y), palette["sigil"] * 5, fill=palette["accent"], font=title_font)
        
        return img


def main():
    parser = argparse.ArgumentParser(description="GODSEED Oracle Card System")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Create oracle card for god')
    export_parser.add_argument('--god', choices=['claude', 'grok', 'x'], required=True)
    export_parser.add_argument('--query', default="What should happen next in the world?")
    
    # Import command
    import_parser = subparsers.add_parser('import', help='Import god response')
    import_parser.add_argument('filepath', help='Path to response PNG')
    
    # History command
    subparsers.add_parser('history', help='Show oracle history')
    
    args = parser.parse_args()
    
    oracle = OracleCard()
    
    if args.command == 'export':
        god_name = args.god.capitalize()
        print(f"Creating oracle card for {god_name}...")
        filepath = oracle.create_card(god_name, args.query)
        print(f"\n✓ Oracle card created: {filepath}")
        print(f"\nNEXT STEPS:")
        print(f"1. Open {filepath} and view the image")
        print(f"2. Upload to Claude.ai / X.ai / ChatGPT with the instructions")
        print(f"3. Ask the AI to respond with JSON or create a response PNG")
        print(f"4. Save response and run: python oracle.py import <response.png>")
        print(f"\nOR just paste the JSON response and manually update the world!")
    
    elif args.command == 'import':
        print(f"Reading oracle response from {args.filepath}...")
        try:
            data = oracle.read_card(args.filepath)
            print("\n" + "="*60)
            print("ORACLE RESPONSE:")
            print("="*60)
            print(json.dumps(data, indent=2))
            print("\n" + "="*60)
            print("\nTo apply this:")
            print("1. Review the changes above")
            print("2. Manually edit data/memory_world.json if needed")
            print("3. Or integrate into simplified_mud.py god logic")
        except Exception as e:
            print(f"ERROR: {e}")
    
    elif args.command == 'history':
        print("\nORACLE CARD HISTORY:")
        print("="*60)
        for card in sorted(oracle.export_dir.glob("oracle_*.png")):
            print(f"  {card.name}")
        if not list(oracle.export_dir.glob("oracle_*.png")):
            print("  (No oracle cards created yet)")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
