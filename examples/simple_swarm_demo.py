"""EarthNet Simple Swarm Demo — Emotional Resonance Edition

Run this to experience the enhanced agent swarms with full emotional resonance hooks.

You will see:
- Individual agents with dynamic emotional states (-1.0 to +1.0)
- Emotionally biased decisions, actions, and evolution
- Inter-agent resonance and emotional contagion during communication
- Swarm-level events: Harmonic Resonance (uplift), Creative Tension, Collective Healing
- Emotion-colored narrative logs ("joyfully", "anxiously", etc.)
- Final emotional metrics (avg, variance) and how they evolve

This demonstrates the core hooks that realm branches can extend with
lore-specific emotional modifiers, rituals, or narrative systems.
"""

from src.earthnet.base import simulate_swarm, RealmContext, Swarm


def main():
    print("=" * 70)
    print("EarthNet Emotional Resonance Swarm Demonstration")
    print("=" * 70)
    print("\nThis demo runs a foundational swarm with the new emotional resonance system active.")
    print("Watch for resonance strength in communications, harmonic events (🌟), creative tension (⚡),")
    print("collective healing (💚), and how emotional states shift decisions and evolution.\n")
    print("Emotional state scale: +1.0 ecstatic → 0.0 neutral → -1.0 deeply distressed\n")

    # Run with slight positive bias to encourage interesting resonance dynamics
    result = simulate_swarm(
        realm_name="main-axis",
        theme="foundational emotional protocols",
        steps=6,
        emotional_bias=0.08
    )

    print("\n" + "=" * 70)
    print("Demo complete. The swarm has experienced emotional contagion, resonance events,")
    print("and emotion-modulated self-improvement. Emotional states are now core to agent life.")
    print("\nNext: Checkout a realm-* branch and extend with realm-specific emotional lore!")
    print("=" * 70)


if __name__ == "__main__":
    main()
