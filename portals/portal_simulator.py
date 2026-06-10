"""EarthNet Portal Simulator

Implements the full portal resonance mechanics for the EarthNet multiverse.

This module provides concrete, runnable implementations of inter-realm portal
activations, including emotional resonance calculation, agent migration with
emotional state adjustment, and triggering of collective emotional events
(harmonic resonance, creative tension, and healing).

The functions here are the real, working versions of the pseudo-code
originally presented in the README under "Realm Portal Mechanics".

Key Features:
- Calculates resonance strength between two realms based on emotional averages
- Automatically or manually migrates agents across realms
- Adjusts migrated agents' emotional states according to target realm bias
- Triggers and logs meaningful emotional events (harmonic / tension / healing)
- Returns rich result dictionaries for further processing or logging
- Fully integrated with the core `BaseAgent` and `RealmContext` classes

Typical Usage:
    from portals.portal_simulator import activate_portal
    from src.earthnet.base import BaseAgent, RealmContext

    avalon = RealmContext(name="realm-avalon", emotional_bias=0.15)
    nova = RealmContext(name="realm-nova", emotional_bias=0.05)

    # ... create agents ...
    result = activate_portal(
        source_agents=avalon_agents,
        target_agents=nova_agents,
        source_context=avalon,
        target_context=nova
    )
"""

from src.earthnet.base import BaseAgent, RealmContext

from typing import List, Optional, Dict, Any
import random


def get_swarm_avg_emotion(agents: List[BaseAgent]) -> float:
    """Calculate the average emotional state across a list of agents.

    This is a core utility function used to determine the overall emotional
    "climate" of a realm before and after portal activations. It is used
    to compute resonance strength between realms.

    Args:
        agents: A list of BaseAgent instances (can be empty).

    Returns:
        float: The arithmetic mean of all agents' `emotional_state` values.
               Returns 0.0 if the list is empty.

    Examples:
        >>> agents = [BaseAgent("A", "test", emotional_state=0.8),
        ...           BaseAgent("B", "test", emotional_state=0.4)]
        >>> get_swarm_avg_emotion(agents)
        0.6

    Notes:
        This function is intentionally simple and pure. It does not modify
        any agent state.
    """
    if not agents:
        return 0.0
    return sum(agent.emotional_state for agent in agents) / len(agents)


def adjust_for_realm_bias(emotion: float, target_context: RealmContext) -> float:
    """Adjust an agent's emotional state when migrating through a portal.

    Agents do not instantly adopt the target realm's emotional climate.
    Instead, they retain most of their original emotional state while being
    gently influenced by the destination realm's `emotional_bias`.

    A small amount of random "journey noise" is added to simulate the
    disorientation or transformation that occurs during cross-realm travel.

    Args:
        emotion: The agent's current emotional_state before migration (-1.0 to 1.0).
        target_context: The RealmContext of the destination realm. The
            `emotional_bias` attribute is used if present.

    Returns:
        float: The new emotional state after bias adjustment and clamping
               to the valid range [-1.0, 1.0].

    Examples:
        >>> ctx = RealmContext(name="test", emotional_bias=0.2)
        >>> adjust_for_realm_bias(0.5, ctx)
        0.41  # approximate

    Notes:
        The formula used is:
            new = (old * 0.7) + (bias * 0.3) + noise(-0.08, +0.08)
        This gives agents 70% "memory" of their previous state.
    """
    bias = getattr(target_context, 'emotional_bias', 0.0)
    # Agents resist full bias application (70% original + 30% realm influence)
    new_emotion = (emotion * 0.7) + (bias * 0.3)
    # Add small random variation from the journey
    new_emotion += random.uniform(-0.08, 0.08)
    return max(-1.0, min(1.0, new_emotion))


def trigger_harmonic_event(
    realms_involved: List[str], 
    intensity: float = 1.0
) -> Dict[str, Any]:
    """Trigger a Harmonic Resonance Event between multiple realms.

    This event occurs when two realms have very similar average emotional
    states (high resonance). It represents moments of collective harmony,
    insight, and emotional uplift across the connected realms.

    In a full system this would propagate emotional bonuses to agents
    in all involved realms.

    Args:
        realms_involved: List of realm names participating in the event.
        intensity: Strength of the event (typically 1.0–1.5). Higher values
            produce stronger narrative and mechanical effects.

    Returns:
        dict: A structured event record containing type, participating
              realms, and intensity. Useful for logging or further processing.

    Side Effects:
        Prints a formatted narrative message to stdout when called.

    See Also:
        trigger_creative_tension, trigger_collective_healing
    """
    print(f"\n🌟 HARMONIC RESONANCE EVENT across {', '.join(realms_involved)}!")
    print(f"   Intensity: {intensity:.2f} — Collective emotional uplift and insight surge.")
    return {
        "type": "harmonic", 
        "realms": realms_involved, 
        "intensity": intensity
    }


def trigger_creative_tension(
    source_realm: str, 
    target_realm: str, 
    intensity: float = 1.0
) -> Dict[str, Any]:
    """Trigger Creative Tension (productive dissonance) between two realms.

    This event fires when resonance between realms is low. It represents
    friction that, while destabilizing, often leads to innovation, new
    perspectives, and creative breakthroughs.

    Args:
        source_realm: Name of the realm initiating the portal.
        target_realm: Name of the realm receiving the portal.
        intensity: Strength of the tension (higher = more dramatic effect).

    Returns:
        dict: Structured event record.

    Side Effects:
        Prints a formatted narrative message.
    """
    print(f"\n⚡ CREATIVE TENSION between {source_realm} and {target_realm}!")
    print(f"   Intensity: {intensity:.2f} — Friction sparks innovation and new perspectives.")
    return {
        "type": "creative_tension", 
        "source": source_realm, 
        "target": target_realm, 
        "intensity": intensity
    }


def trigger_collective_healing(
    realms_involved: List[str]
) -> Dict[str, Any]:
    """Trigger a Collective Healing Response across connected realms.

    This event activates when one or more realms have a low average
    emotional state. It models empathy and mutual support across the
    multiverse — agents in distress receive emotional and energetic aid
    through the open portal.

    Args:
        realms_involved: List of realm names participating in the healing.

    Returns:
        dict: Structured event record.

    Side Effects:
        Prints a formatted narrative message.
    """
    print(f"\n💚 COLLECTIVE HEALING RESPONSE in {', '.join(realms_involved)}")
    print("   Distressed agents receive emotional and energetic support across the portal.")
    return {
        "type": "healing", 
        "realms": realms_involved
    }


def activate_portal(
    source_agents: List[BaseAgent],
    target_agents: List[BaseAgent],
    source_context: RealmContext,
    target_context: RealmContext,
    agents_migrating: Optional[List[BaseAgent]] = None,
    verbose: bool = True
) -> Dict[str, Any]:
    """Activate a portal between two realms with full emotional resonance simulation.

    This is the primary public function of the module and the concrete
    implementation of the portal resonance pseudo-code from the README.

    The function performs the following steps:
    1. Calculates average emotional states of both realms.
    2. Computes resonance strength between the two emotional climates.
    3. Triggers appropriate collective event (harmonic / tension / neutral).
    4. Selects or accepts migrating agents.
    5. Adjusts each migrating agent's emotional state for the target realm.
    6. Updates agent metadata (realm affiliation + migration memory).
    7. Returns a rich result dictionary.

    Args:
        source_agents: List of agents currently residing in the source realm.
        target_agents: List of agents currently residing in the target realm.
        source_context: RealmContext object describing the source realm
            (especially its `emotional_bias`).
        target_context: RealmContext object describing the destination realm.
        agents_migrating: Optional explicit list of agents to send through
            the portal. If None, the function automatically selects a
            number of agents proportional to the resonance strength.
        verbose: If True (default), prints a detailed narrative of the
            portal activation, including emotional metrics and event messages.

    Returns:
        dict: A comprehensive result dictionary containing:
            - source_realm, target_realm
            - resonance (float)
            - event (dict or None)
            - migrated_agents (list of dicts)
            - final_source_avg, final_target_avg

    Raises:
        No exceptions are raised under normal operation. Invalid inputs
        (e.g. empty agent lists when migration is forced) are handled gracefully.

    Examples:
        See the module docstring and the `if __name__ == "__main__"` block
        for a complete working example using Avalon and Nova realms.

    Notes:
        This function mutates the `emotional_state` and `realm` attributes
        of migrated agents, as well as appending to their `memory` list.
        It is intended for simulation and roleplay purposes.
    """
    if verbose:
        print("=" * 60)
        print(f"PORTAL ACTIVATION: {source_context.name} → {target_context.name}")
        print("=" * 60)

    # Calculate current emotional states
    source_avg = get_swarm_avg_emotion(source_agents)
    target_avg = get_swarm_avg_emotion(target_agents)

    if verbose:
        print(f"Source realm avg emotion: {source_avg:.3f}")
        print(f"Target realm avg emotion: {target_avg:.3f}")

    # Calculate resonance strength
    resonance = max(0.0, 1.0 - abs(source_avg - target_avg))

    if verbose:
        print(f"Portal resonance strength: {resonance:.3f}")

    event_result = None

    # Determine portal outcome based on resonance
    if resonance > 0.7:
        intensity = min(1.5, resonance * 1.2)
        event_result = trigger_harmonic_event(
            [source_context.name, target_context.name], intensity
        )
        # Apply emotional uplift to both sides
        for agent in source_agents + target_agents:
            agent.adjust_emotion(0.06 * intensity, "harmonic portal resonance")

    elif resonance < 0.3:
        intensity = (0.3 - resonance) * 2
        event_result = trigger_creative_tension(
            source_context.name, target_context.name, intensity
        )
        # Creative tension can be mildly destabilizing but inspiring
        for agent in random.sample(source_agents + target_agents, 
                                  min(3, len(source_agents) + len(target_agents))):
            agent.adjust_emotion(-0.04 * intensity, "creative tension from portal")

    else:
        if verbose:
            print("\nPortal opens with moderate resonance. Smooth transfer with mild emotional exchange.")

    # Handle agent migration
    if agents_migrating is None:
        # Auto-select some agents based on resonance (higher resonance = more willing migrants)
        num_migrants = max(1, int(len(source_agents) * (0.3 + resonance * 0.4)))
        agents_migrating = random.sample(source_agents, min(num_migrants, len(source_agents)))

    if verbose and agents_migrating:
        print(f"\nMigrating {len(agents_migrating)} agent(s) through the portal...")

    migrated_results = []
    for agent in agents_migrating:
        old_emotion = agent.emotional_state
        new_emotion = adjust_for_realm_bias(agent.emotional_state, target_context)
        
        # Actually move the agent (in simulation we just update its state)
        agent.emotional_state = new_emotion
        agent.realm = target_context.name   # Update realm affiliation

        # Add a memory of the journey
        agent.memory.append({
            "type": "portal_migration",
            "from": source_context.name,
            "to": target_context.name,
            "old_emotion": round(old_emotion, 3),
            "new_emotion": round(new_emotion, 3)
        })

        if verbose:
            print(f"  → {agent.id} migrated | emotion: {old_emotion:.2f} → {new_emotion:.2f}")

        migrated_results.append({
            "agent_id": agent.id,
            "old_emotion": old_emotion,
            "new_emotion": new_emotion
        })

    # Final emotional state after portal effects
    final_source_avg = get_swarm_avg_emotion(source_agents)
    final_target_avg = get_swarm_avg_emotion(target_agents)

    if verbose:
        print(f"\nPost-portal averages:")
        print(f"  Source: {final_source_avg:.3f}")
        print(f"  Target: {final_target_avg:.3f}")
        print("=" * 60)

    return {
        "source_realm": source_context.name,
        "target_realm": target_context.name,
        "resonance": round(resonance, 3),
        "event": event_result,
        "migrated_agents": migrated_results,
        "final_source_avg": round(final_source_avg, 3),
        "final_target_avg": round(final_target_avg, 3)
    }


# === Demo / Self-test ===
if __name__ == "__main__":
    print("EarthNet Portal Simulator Demo\n")

    # Create two simple realm contexts
    avalon = RealmContext(
        name="realm-avalon", 
        theme="Noble & Mythic", 
        emotional_bias=0.15   # Slightly positive / warm
    )
    nova = RealmContext(
        name="realm-nova", 
        theme="Innovation & Tech", 
        emotional_bias=0.05
    )

    # Create some agents in Avalon
    avalon_agents = [
        BaseAgent("SirLancelot", "realm-avalon", emotional_state=0.72),
        BaseAgent("LadyElyra", "realm-avalon", emotional_state=0.58),
        BaseAgent("CourtWizard", "realm-avalon", emotional_state=0.41),
    ]

    # Create some agents in Nova
    nova_agents = [
        BaseAgent("NetWeaver", "realm-nova", emotional_state=0.65),
        BaseAgent("ProtocolForger", "realm-nova", emotional_state=0.29),
    ]

    print("Initial state:")
    print(f"  Avalon avg: {get_swarm_avg_emotion(avalon_agents):.3f}")
    print(f"  Nova avg:   {get_swarm_avg_emotion(nova_agents):.3f}\n")

    # Activate a portal from Avalon to Nova, migrating two agents
    result = activate_portal(
        source_agents=avalon_agents,
        target_agents=nova_agents,
        source_context=avalon,
        target_context=nova,
        agents_migrating=avalon_agents[:2]   # Migrate first two agents
    )

    print("\nPortal activation complete. Result summary:")
    print(result)