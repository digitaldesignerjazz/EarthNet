"""EarthNet Simple Swarm Demo

Run this from the main branch to see the foundational agent swarm in action.
It uses the core BaseAgent and Swarm classes to simulate emergent behavior,
self-improvement, and collective dynamics.

This serves as the template that realm-specific run_realm_swarm.py files extend and flavor.
"""

from src.earthnet.base import simulate_swarm, RealmContext, Swarm


def main():
    print("=" * 60)
    print("EarthNet Foundational Swarm Demonstration")
    print("=" * 60)
    print("\nThis demo instantiates a basic swarm in the 'main' realm context")
    print("and runs several simulation steps. Watch for emergence messages,")
    print("energy fluctuations, reflections, and post-run evolution.")
    print("\nIn realm branches, specialized agents and lore will produce very different")
    print("narratives and dynamics while reusing the same core engine.\n")

    # Run the convenience function
    result = simulate_swarm(realm_name="main-axis", theme="foundational protocols", steps=5)

    print("\n" + "=" * 60)
    print("Demo complete. The swarm has evolved.")
    print("Explore realm-* branches for richer, themed experiences.")
    print("=" * 60)


if __name__ == "__main__":
    main()
