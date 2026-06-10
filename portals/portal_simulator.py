"""EarthNet Portal Simulator

Implements real version of the portal resonance mechanics described in the README.
This module allows simulation of inter-realm portal activations with emotional
resonance effects, agent migration, and collective events.

Usage:
    from portals.portal_simulator import activate_portal
    from src.earthnet.base import BaseAgent, RealmContext

    # Create agents and realms...
    activate_portal(source_agents, target_agents, source_context, target_context)
"""

from src.earthnet.base import BaseAgent, RealmContext

from typing import List, Optional
import random


def get_swarm_avg_emotion(agents: List[BaseAgent]) -> float:
    """Calculate average emotional state of a list of agents."""
    if not agents:
        return 0.0
    return sum(agent.emotional_state for agent in agents) / len(agents)


def adjust_for_realm_bias(emotion: float, target_context: RealmContext) -> float:
    """Adjust an agent's emotional state when migrating to a new realm.

    Applies the target realm's emotional_bias with some natural resistance.
    """
    bias = getattr(target_context, 'emotional_bias', 0.0)
    # Agents resist full bias application (70% original + 30% realm influence)
    new_emotion = (emotion * 0.7) + (bias * 0.3)
    # Add small random variation from the journey
    new_emotion += random.uniform(-0.08, 0.08)
    return max(-1.0, min(1.0, new_emotion))


def trigger_harmonic_event(realms_involved: List[str], intensity: float = 1.0):
    """Trigger a harmonic resonance event across involved realms."""
    print(f"\n🌟 HARMONIC RESONANCE EVENT across {', '.join(realms_involved)}!")
    print(f"   Intensity: {intensity:.2f} — Collective emotional uplift and insight surge.")
    # In a full implementation this would modify agent states in both realms
    return {"type": "harmonic", "realms": realms_involved, "intensity": intensity}


def trigger_creative_tension(source_realm: str, target_realm: str, intensity: float = 1.0):
    """Trigger creative tension / productive dissonance between realms."""
    print(f"\n⚡ CREATIVE TENSION between {source_realm} and {target_realm}!")
    print(f"   Intensity: {intensity:.2f} — Friction sparks innovation and new perspectives.")
    return {"type": "creative_tension", "source": source_realm, "target": target_realm, "intensity": intensity}


def trigger_collective_healing(realms_involved: List[str]):
    """Trigger swarm healing response when emotional average is low."""
    print(f"\n💚 COLLECTIVE HEALING RESPONSE in {', '.join(realms_involved)}")
    print("   Distressed agents receive emotional and energetic support across the portal.")
    return {"type": "healing", "realms": realms_involved}


def activate_portal(
    source_agents: List[BaseAgent],
    target_agents: List[BaseAgent],
    source_context: RealmContext,
    target_context: RealmContext,
    agents_migrating: Optional[List[BaseAgent]] = None,
    verbose: bool = True
) -> dict:
    """Activate a portal between two realms with full emotional resonance simulation.

    This is the real implementation of the pseudo-code from the README.

    Args:
        source_agents: Agents currently in the source realm
        target_agents: Agents currently in the target realm
        source_context: RealmContext of the source realm
        target_context: RealmContext of the target realm
        agents_migrating: Specific agents to migrate (if None, selects some based on resonance)
        verbose: Whether to print narrative output

    Returns:
        Dictionary with results of the portal activation
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