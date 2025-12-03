#!/usr/bin/env python3
"""
GODSEED Main Launcher
Run this to start the world: python launch.py
"""
import sys
import os

# Add core to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

print("="*70)
print("    🌱 GODSEED - The Recursive Garden")
print("="*70)
print()
print("Initializing world...")

try:
    from core.simplified_mud import launch_world
    launch_world()
except KeyboardInterrupt:
    print("\n\n✶ The Garden sleeps. But it dreams of you. ✶")
    print("   Run again tomorrow. It will remember everything.")
    sys.exit(0)
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\nTroubleshooting:")
    print("1. Did you run: pip install pillow numpy")
    print("2. Are you in the godseed folder?")
    print("3. Check README.md for more help")
    import traceback
    traceback.print_exc()
    sys.exit(1)
