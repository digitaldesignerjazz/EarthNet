"""EarthNet Base Classes - Foundational Agent Swarm Primitives

This module provides the core abstractions for autonomous agents and swarms.
Designed for extension in specialized realms (see realm-* branches).

Design Philosophy:
- Minimal dependencies (stdlib only) for maximum portability and conceptual clarity.
- Emphasis on emergence: simple local rules yield complex collective behavior.
- Self-improvement hooks: agents and swarms can analyze their own history and mutate.
- Realm-aware: every entity carries realm context and can adapt behavior accordingly.
- Extensible: subclass BaseAgent and override key methods for realm flavor.

Future extensions (in ARCHITECTURE.md and realm branches):
- Asyncio for concurrent agent thinking
- Persistent memory (JSON/ SQLite per realm)
- Integration with real mesh (Yggdrasil) or blockchain (QCoin simulation)
- Emotional state vectors and resonance mechanics
- Genetic/evolutionary algorithms for agent genomes
"""

import random
import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class RealmContext:
    """Holds the environmental and thematic context for a realm."""
    name: str
    theme: str
    rules: List[str] = field(default_factory=list)
    resources: Dict[str, Any] = field(default_factory=dict)
    lore: str = ""


class BaseAgent:
    """Core autonomous agent class.

    Agents have identity, state (energy, memory), dynamic goals, and a set of
    actions. They can perceive simple environments, decide, act, communicate with
    peers, reflect on experience, and evolve (self-improve).

    Subclass this in realm-specific modules and override methods to inject
    thematic behavior (e.g., spell-casting in Avalon, packet-routing in Nova).
    """

    def __init__(self, agent_id: str, realm: str, **kwargs):
        self.id = agent_id
        self.realm = realm
        self.energy = kwargs.get('energy', 100.0)
        self.memory: List[Dict[str, Any]] = []
        self.goals: List[str] = kwargs.get('goals', ['explore', 'collaborate', 'evolve'])
        self.knowledge: Dict[str, Any] = {}  # Simple semantic store
        self.lineage: List[str] = kwargs.get('lineage', ['seed'])
        self.emotional_state: float = 0.5  # -1 to 1, for future emotional AI resonance

    def perceive(self, environment: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Observe the current environment or swarm state."""
        if environment is None:
            environment = {'type': 'neutral', 'density': random.random()}
        perception = {
            'timestamp': len(self.memory),
            'environment': environment,
            'self_energy': self.energy,
            'active_goals': self.goals.copy()
        }
        return perception

    def decide(self, perception: Dict[str, Any]) -> str:
        """Choose next action based on perception and internal state.

        Simple heuristic; override for sophisticated decision policies.
        """
        if self.energy < 30:
            return 'rest'
        if len(self.memory) > 8 and random.random() < 0.3:
            return 'reflect'
        if random.random() < 0.4:
            return 'communicate'
        return random.choice(['act', 'explore', 'innovate'])

    def act(self) -> str:
        """Perform an action in the realm. Returns a descriptive log string."""
        self.energy = max(0, self.energy - random.uniform(3, 8))
        action_desc = f"{self.id} performs a {random.choice(['subtle', 'bold', 'curious', 'strategic'])} action"
        log = {
            'type': 'action',
            'description': action_desc,
            'energy_delta': -5,
            'realm': self.realm
        }
        self.memory.append(log)
        return action_desc

    def communicate(self, other: 'BaseAgent') -> str:
        """Exchange information or intent with another agent."""
        if self.energy < 10:
            return f"{self.id} is too depleted to communicate with {other.id}"
        self.energy -= 2
        insight = f"Insight from {self.realm}: {random.choice(['pattern', 'anomaly', 'opportunity', 'warning'])} detected"
        msg = f"{self.id} shares with {other.id}: {insight}"
        other.memory.append({'type': 'received_comm', 'from': self.id, 'content': insight})
        self.memory.append({'type': 'sent_comm', 'to': other.id, 'content': insight})
        return msg

    def reflect(self) -> str:
        """Analyze own memory and state to gain insight or adjust goals."""
        if not self.memory:
            return f"{self.id} has no experiences to reflect upon yet."
        recent = self.memory[-min(5, len(self.memory)):]
        avg_energy = sum(m.get('energy_delta', 0) for m in recent if isinstance(m, dict)) / max(1, len(recent))
        reflection = f"{self.id} reflects: recent avg energy delta {avg_energy:.1f}. "
        if avg_energy < -6:
            reflection += "Need more efficient strategies or rest."
            if 'rest' not in self.goals:
                self.goals.append('rest_efficiently')
        else:
            reflection += "Momentum is good; considering innovation."
            if 'innovate' not in self.goals:
                self.goals.append('innovate')
        self.memory.append({'type': 'reflection', 'content': reflection})
        self.emotional_state = max(-1.0, min(1.0, self.emotional_state + random.uniform(-0.1, 0.15)))
        return reflection

    def evolve(self) -> str:
        """Self-improvement step: mutate goals, strategies, or capabilities based on history.

        This is the recursive self-improvement hook central to EarthNet philosophy.
        In advanced realms this can become sophisticated (e.g. prompt mutation, weight updates).
        """
        if len(self.memory) < 6:
            return f"{self.id} has insufficient experience to evolve meaningfully."
        # Simple evolution: add specialized goal based on realm or recent activity
        new_goal = f"master_{self.realm.split('-')[-1] if '-' in self.realm else self.realm}"
        if new_goal not in self.goals:
            self.goals.append(new_goal)
            self.energy = min(120, self.energy + 15)  # Reward for evolution
        evolution_log = f"{self.id} evolves new goal: {new_goal}. Energy boosted."
        self.memory.append({'type': 'evolution', 'content': evolution_log})
        return evolution_log

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'realm': self.realm,
            'energy': self.energy,
            'goals': self.goals,
            'emotional_state': self.emotional_state,
            'memory_length': len(self.memory)
        }


class Swarm:
    """Manages a collective of BaseAgents (or subclasses) within a realm.

    Orchestrates simulation steps, facilitates interactions, detects emergence,
    and triggers collective evolution.
    """

    def __init__(self, name: str, realm_context: RealmContext, num_agents: int = 6):
        self.name = name
        self.realm_context = realm_context
        self.agents: List[BaseAgent] = []
        for i in range(num_agents):
            agent_id = f"{name}_{realm_context.name}_{i:02d}"
            self.agents.append(BaseAgent(agent_id, realm_context.name))

    def step(self, environment: Optional[Dict[str, Any]] = None) -> List[str]:
        """Advance one simulation epoch. Returns list of log strings."""
        logs: List[str] = []
        logs.append(f"\n=== Swarm Step in {self.realm_context.name} ({self.realm_context.theme}) ===")

        for agent in self.agents:
            perception = agent.perceive(environment)
            action = agent.decide(perception)

            if action == 'act' or action == 'explore':
                logs.append(agent.act())
            elif action == 'communicate':
                other = random.choice([a for a in self.agents if a.id != agent.id])
                logs.append(agent.communicate(other))
            elif action == 'reflect':
                logs.append(agent.reflect())
            elif action == 'rest':
                agent.energy = min(100, agent.energy + random.uniform(5, 12))
                logs.append(f"{agent.id} rests and recovers energy ({agent.energy:.1f})")
            elif action == 'innovate':
                logs.append(f"{agent.id} innovates a new approach in {self.realm_context.name}")
                agent.energy = max(0, agent.energy - 3)

        # Emergent collective behavior detection
        avg_energy = sum(a.energy for a in self.agents) / len(self.agents)
        if avg_energy < 45:
            logs.append("EMERGENCE: Swarm enters collective low-energy phase. Agents begin supporting each other.")
            for agent in self.agents:
                if agent.energy < 40:
                    agent.energy += 8  # Swarm healing
                    logs.append(f"  -> {agent.id} receives swarm support (+8 energy)")
        elif avg_energy > 85 and random.random() < 0.3:
            logs.append("EMERGENCE: High collective energy triggers innovation surge!")

        # Occasional collective reflect
        if random.random() < 0.25:
            logs.append("Collective reflection moment...")
            for agent in random.sample(self.agents, min(2, len(self.agents))):
                logs.append(agent.reflect())

        return logs

    def run_simulation(self, steps: int = 4, verbose: bool = True) -> str:
        """Run multiple steps and return aggregated narrative + stats."""
        all_logs: List[str] = []
        for step_num in range(steps):
            step_logs = self.step()
            all_logs.extend(step_logs)
            if verbose:
                print("\n".join(step_logs))

        # Final evolution pass for self-improvement demonstration
        all_logs.append("\n--- Post-simulation Evolution Phase ---")
        for agent in self.agents:
            evol = agent.evolve()
            all_logs.append(evol)
            if verbose:
                print(evol)

        # Summary stats
        final_energies = [a.energy for a in self.agents]
        summary = (f"\nSwarm '{self.name}' in {self.realm_context.name} completed {steps} steps.\n"
                   f"Average final energy: {sum(final_energies)/len(final_energies):.1f} | "
                   f"Range: {min(final_energies):.1f} - {max(final_energies):.1f}")
        all_logs.append(summary)
        if verbose:
            print(summary)
        return "\n".join(all_logs)


# Convenience factory

def simulate_swarm(realm_name: str = "main", theme: str = "foundational", steps: int = 4) -> str:
    """Quick entrypoint to instantiate and run a basic swarm."""
    context = RealmContext(name=realm_name, theme=theme)
    swarm = Swarm(name="CoreSwarm", realm_context=context, num_agents=5)
    return swarm.run_simulation(steps=steps, verbose=True)


if __name__ == "__main__":
    print("EarthNet Base Module Self-Test")
    result = simulate_swarm()
    print("\n=== Self-Test Complete ===")
