"""EarthNet Base Classes - Foundational Agent Swarm Primitives with Emotional Resonance

Core module providing the fundamental building blocks for emotionally resonant
agent swarms across the EarthNet multiverse.

This module is the heart of the simulation engine. It is designed to be
subclassed and extended by individual realm branches.

Quick Start Example:
    from src.earthnet.base import BaseAgent, Swarm, RealmContext, simulate_swarm

    context = RealmContext(name="test-realm", theme="Demo", emotional_bias=0.1)
    result = simulate_swarm(realm_name="demo", theme="example", steps=5)

    agent = BaseAgent("Agent1", "demo-realm", emotional_state=0.6)
    agent.adjust_emotion(0.3, "positive event")
    print(agent.get_emotional_color())   # 'joyfully'

See also:
- portals/portal_simulator.py for cross-realm portal mechanics
- README.md for full architecture and emotional resonance documentation
"""

import random
import json
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class RealmContext:
    """Holds the environmental and thematic context for a realm.

    Realms can extend this with emotional modifiers (e.g., Avalon 'grace' bias,
    Cyberia 'paranoia' pull, Quantum 'superposition' emotional volatility).

    Usage Example:
        >>> ctx = RealmContext(name="realm-mythweaver", theme="Story & Song", emotional_bias=0.12)
    """
    name: str
    theme: str
    rules: List[str] = field(default_factory=list)
    resources: Dict[str, Any] = field(default_factory=dict)
    lore: str = ""
    emotional_bias: float = 0.0


class BaseAgent:
    """Core autonomous agent class with full emotional resonance hooks.

    Usage Example:
        >>> agent = BaseAgent("Explorer", "forest", emotional_state=0.4)
        >>> agent.adjust_emotion(0.5, "found ancient artifact")
        >>> print(agent.get_emotional_color())
        'joyfully'
    """

    def __init__(self, agent_id: str, realm: str, **kwargs):
        self.id = agent_id
        self.realm = realm
        self.energy = kwargs.get('energy', 100.0)
        self.memory: List[Dict[str, Any]] = []
        self.goals: List[str] = kwargs.get('goals', ['explore', 'collaborate', 'evolve'])
        self.knowledge: Dict[str, Any] = {}
        self.lineage: List[str] = kwargs.get('lineage', ['seed'])
        self.emotional_state: float = kwargs.get('emotional_state', 0.5)
        self._clamp_emotion()

    def _clamp_emotion(self):
        self.emotional_state = max(-1.0, min(1.0, self.emotional_state))

    def get_emotional_color(self) -> str:
        """Returns a flavorful descriptor for narrative logs and roleplay output."""
        if self.emotional_state > 0.75:
            return "ecstatically"
        elif self.emotional_state > 0.4:
            return "joyfully"
        elif self.emotional_state > 0.1:
            return "warmly"
        elif self.emotional_state > -0.2:
            return "calmly"
        elif self.emotional_state > -0.5:
            return "warily"
        elif self.emotional_state > -0.75:
            return "anxiously"
        else:
            return "deeply distressed"

    def adjust_emotion(self, delta: float, reason: str = "") -> float:
        """Primary hook to shift emotional state."""
        old_state = self.emotional_state
        self.emotional_state += delta
        self._clamp_emotion()
        change = self.emotional_state - old_state

        log_entry = {
            'type': 'emotion_adjust',
            'delta': round(delta, 3),
            'new_state': round(self.emotional_state, 3),
            'change': round(change, 3),
            'reason': reason or 'unspecified'
        }
        self.memory.append(log_entry)
        return self.emotional_state

    def perceive(self, environment: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Observe environment, now emotionally tinted."""
        if environment is None:
            environment = {'type': 'neutral', 'density': random.random()}
        tint = 'opportunity' if self.emotional_state > 0.2 else ('threat' if self.emotional_state < -0.2 else 'neutral')
        perception = {
            'timestamp': len(self.memory),
            'environment': environment,
            'emotional_tint': tint,
            'self_energy': self.energy,
            'self_emotion': round(self.emotional_state, 2),
            'active_goals': self.goals.copy()
        }
        return perception

    def decide(self, perception: Dict[str, Any]) -> str:
        """Emotionally modulated decision making."""
        emotion = self.emotional_state
        if self.energy < 25:
            return 'rest'

        if emotion > 0.65:
            weights = {'innovate': 0.35, 'communicate': 0.30, 'act': 0.20, 'explore': 0.15}
        elif emotion > 0.25:
            weights = {'communicate': 0.30, 'act': 0.25, 'innovate': 0.20, 'explore': 0.25}
        elif emotion > -0.25:
            weights = {'act': 0.30, 'explore': 0.25, 'communicate': 0.25, 'reflect': 0.20}
        elif emotion > -0.6:
            weights = {'rest': 0.25, 'reflect': 0.30, 'explore': 0.25, 'communicate': 0.20}
        else:
            weights = {'rest': 0.45, 'reflect': 0.35, 'explore': 0.15, 'communicate': 0.05}

        choices = list(weights.keys())
        probs = list(weights.values())
        return random.choices(choices, weights=probs, k=1)[0]

    def act(self) -> str:
        """Perform action, with emotional flavor and modulated energy impact."""
        color = self.get_emotional_color()
        base_cost = random.uniform(3, 8)

        if self.emotional_state > 0.5:
            energy_delta = -base_cost * 0.7
            flavor = f"{color} innovates or expresses boldly"
            self.adjust_emotion(0.03, "successful bold action")
        elif self.emotional_state < -0.4:
            energy_delta = -base_cost * 1.4
            flavor = f"{color} acts defensively or minimally"
            self.adjust_emotion(-0.02, "defensive action while distressed")
        else:
            energy_delta = -base_cost
            flavor = f"{color} performs a deliberate action"

        self.energy = max(0, self.energy + energy_delta)
        log = {
            'type': 'action',
            'description': flavor,
            'energy_delta': round(energy_delta, 1),
            'emotional_state': round(self.emotional_state, 2),
            'realm': self.realm
        }
        self.memory.append(log)
        return flavor

    def communicate(self, other: 'BaseAgent') -> Tuple[str, float]:
        """Exchange information with another agent while performing emotional resonance.

        This is one of the core mechanisms for inter-agent emotional contagion.
        The resonance strength is calculated based on how close their emotional
        states are. Both agents then move slightly toward each other's emotional
        average.

        Usage Example (Resonance):
            >>> agent1 = BaseAgent("A1", "test", emotional_state=0.8)
            >>> agent2 = BaseAgent("A2", "test", emotional_state=0.2)
            >>> msg, res = agent1.communicate(agent2)
            >>> print(f"Resonance strength: {res:.2f}")
            # High resonance because they are emotionally close after adjustment
        """
        if self.energy < 8:
            return f"{self.id} is too depleted to reach out to {other.id}", 0.0

        diff = abs(self.emotional_state - other.emotional_state)
        resonance = max(0.0, 1.0 - diff)

        avg_emotion = (self.emotional_state + other.emotional_state) / 2
        shift = (avg_emotion - self.emotional_state) * (0.15 + 0.25 * resonance)

        self.adjust_emotion(shift, f"resonance with {other.id}")
        other.adjust_emotion((avg_emotion - other.emotional_state) * (0.15 + 0.25 * resonance),
                             f"resonance with {self.id}")

        color = self.get_emotional_color()
        insight = f"{random.choice(['pattern', 'anomaly', 'opportunity', 'warning', 'harmony', 'tension'])} in the {self.realm} field"
        msg = f"{color} {self.id} resonates with {other.id} (resonance={resonance:.2f}): {insight}"

        self.energy -= 2.5
        other.energy = max(0, other.energy - 1.5)

        comm_log = {
            'type': 'resonant_comm',
            'to': other.id,
            'resonance': round(resonance, 3),
            'insight': insight,
            'emotional_state_after': round(self.emotional_state, 2)
        }
        self.memory.append(comm_log)
        return msg, resonance

    def resonate_with(self, other: 'BaseAgent') -> float:
        """Dedicated method to perform emotional resonance with another agent.

        This is a convenience wrapper around communicate() focused purely on
        the emotional exchange. Very useful when you want to simulate resonance
        without generating full communication logs.

        Usage Example (Resonate Examples):
            >>> agent1 = BaseAgent("Harmonious", "test", emotional_state=0.7)
            >>> agent2 = BaseAgent("Dissonant", "test", emotional_state=-0.4)
            >>> resonance = agent1.resonate_with(agent2)
            >>> print(f"Resonance strength between agents: {resonance:.2f}")
            # Lower resonance because their emotional states are far apart

            >>> # After resonance, their emotions move closer together
            >>> print(agent1.emotional_state, agent2.emotional_state)
        """
        _, resonance = self.communicate(other)
        return resonance

    def reflect(self) -> str:
        """Emotionally aware reflection."""
        if not self.memory:
            return f"{self.id} has no experiences to reflect upon yet."

        recent = self.memory[-min(6, len(self.memory)):]

        reflection = f"{self.get_emotional_color()} {self.id} reflects on recent events. "

        if self.emotional_state > 0.4:
            reflection += "Positive momentum suggests expanding goals."
            if 'innovate' not in self.goals:
                self.goals.append('innovate_boldly')
            self.adjust_emotion(0.05, "optimistic reflection")
        elif self.emotional_state < -0.3:
            reflection += "Distress signals need for rest and healing."
            if 'heal' not in self.goals:
                self.goals.append('heal_and_recover')
            self.adjust_emotion(0.08, "healing reflection")
        else:
            reflection += "Balanced perspective."

        self.memory.append({'type': 'reflection', 'content': reflection, 'emotion': round(self.emotional_state, 2)})
        return reflection

    def evolve(self) -> str:
        """Self-improvement modulated by emotional state."""
        if len(self.memory) < 5:
            return f"{self.id} has insufficient experience to evolve meaningfully."

        emotion = self.emotional_state
        base_new_goal = f"master_{self.realm.split('-')[-1] if '-' in self.realm else self.realm}"

        if emotion > 0.6:
            new_goal = f"transcend_{base_new_goal}"
            energy_reward = 22
            self.adjust_emotion(0.08, "ecstatic evolution")
        elif emotion > 0.2:
            new_goal = base_new_goal
            energy_reward = 15
            self.adjust_emotion(0.04, "positive evolution")
        else:
            new_goal = f"stabilize_and_{base_new_goal}"
            energy_reward = 10
            self.adjust_emotion(0.06, "cautious stabilizing evolution")

        if new_goal not in self.goals:
            self.goals.append(new_goal)
            self.energy = min(130, self.energy + energy_reward)

        evolution_log = f"{self.get_emotional_color()} {self.id} evolves '{new_goal}' (emotion={emotion:.2f}). +{energy_reward} energy."
        self.memory.append({'type': 'evolution', 'content': evolution_log, 'emotion': round(emotion, 2)})
        return evolution_log

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'realm': self.realm,
            'energy': round(self.energy, 1),
            'emotional_state': round(self.emotional_state, 3),
            'goals': self.goals,
            'memory_length': len(self.memory)
        }


class Swarm:
    """Manages a collective of agents with emotional resonance orchestration.

    Usage Example:
        >>> context = RealmContext(name="demo", theme="Test")
        >>> swarm = Swarm("TestSwarm", context, num_agents=4)
        >>> swarm.run_simulation(steps=3)
    """

    def __init__(self, name: str, realm_context: RealmContext, num_agents: int = 6):
        self.name = name
        self.realm_context = realm_context
        self.agents: List[BaseAgent] = []
        for i in range(num_agents):
            agent_id = f"{name}_{realm_context.name}_{i:02d}"
            init_emotion = 0.5 + random.uniform(-0.25, 0.25) + realm_context.emotional_bias
            self.agents.append(BaseAgent(agent_id, realm_context.name, emotional_state=init_emotion))

    def _compute_emotional_metrics(self) -> Dict[str, float]:
        emotions = [a.emotional_state for a in self.agents]
        if not emotions:
            return {'avg': 0.0, 'variance': 0.0, 'min': 0.0, 'max': 0.0}
        avg = sum(emotions) / len(emotions)
        variance = sum((e - avg) ** 2 for e in emotions) / len(emotions)
        return {
            'avg': round(avg, 3),
            'variance': round(variance, 3),
            'min': round(min(emotions), 3),
            'max': round(max(emotions), 3)
        }

    def step(self, environment: Optional[Dict[str, Any]] = None) -> List[str]:
        """Advance one simulation epoch with emotional resonance phase."""
        logs: List[str] = []
        logs.append(f"\n=== Swarm Step in {self.realm_context.name} ({self.realm_context.theme}) ===")

        for agent in self.agents:
            perception = agent.perceive(environment)
            action = agent.decide(perception)

            if action in ('act', 'explore', 'innovate'):
                logs.append(agent.act())
            elif action == 'communicate':
                other = random.choice([a for a in self.agents if a.id != agent.id])
                msg, res = agent.communicate(other)
                logs.append(msg)
            elif action == 'reflect':
                logs.append(agent.reflect())
            elif action == 'rest':
                recovery = random.uniform(6, 14)
                agent.energy = min(110, agent.energy + recovery)
                agent.adjust_emotion(0.04, "rest and emotional recovery")
                logs.append(f"{agent.get_emotional_color()} {agent.id} rests and recovers ({agent.energy:.1f} energy, emotion={agent.emotional_state:.2f})")

        for _ in range(max(1, len(self.agents) // 3)):
            a1, a2 = random.sample(self.agents, 2)
            if a1.id != a2.id:
                msg, res = a1.communicate(a2)
                if res > 0.65:
                    logs.append(f"  ✨ Strong resonance ({res:.2f}) between {a1.id} and {a2.id}")

        metrics = self._compute_emotional_metrics()
        avg_e = metrics['avg']
        var_e = metrics['variance']

        if avg_e > 0.55 and var_e < 0.12:
            bonus = 8 + int((avg_e - 0.55) * 20)
            for agent in self.agents:
                agent.energy = min(130, agent.energy + bonus * 0.6)
                agent.adjust_emotion(0.06, "harmonic swarm resonance")
            logs.append(f"🌟 HARMONIC RESONANCE EVENT!")

        return logs

    def run_simulation(self, steps: int = 4, verbose: bool = True) -> str:
        """Run multiple steps and return aggregated narrative + stats."""
        all_logs: List[str] = []
        for step_num in range(steps):
            step_logs = self.step()
            all_logs.extend(step_logs)

        all_logs.append("\n--- Post-simulation Evolution Phase ---")
        for agent in self.agents:
            evol = agent.evolve()
            all_logs.append(evol)

        final_metrics = self._compute_emotional_metrics()
        summary = f"\nSwarm '{self.name}' completed {steps} steps. Final avg emotion: {final_metrics['avg']:.2f}"
        all_logs.append(summary)

        if verbose:
            print("\n".join(all_logs))
        return "\n".join(all_logs)


def simulate_swarm(realm_name: str = "main", theme: str = "foundational", steps: int = 4,
                 emotional_bias: float = 0.0) -> str:
    """Quick entrypoint to run a swarm with emotional resonance.

    Usage Example:
        >>> result = simulate_swarm(realm_name="avalon", steps=6, emotional_bias=0.1)
    """
    context = RealmContext(name=realm_name, theme=theme, emotional_bias=emotional_bias)
    swarm = Swarm(name="CoreSwarm", realm_context=context, num_agents=5)
    return swarm.run_simulation(steps=steps, verbose=True)


if __name__ == "__main__":
    print("=" * 70)
    print("EarthNet Base Module - Usage Examples (Including Resonance)")
    print("=" * 70)

    print("\n1. Basic Agent Creation and Emotional Modulation")
    agent = BaseAgent("TestAgent", "demo-realm", emotional_state=0.3)
    agent.adjust_emotion(0.6, "major discovery")
    print(f"   After event: {agent.emotional_state} ({agent.get_emotional_color()})")

    print("\n2. Running a Swarm Simulation")
    result = simulate_swarm(realm_name="demo", theme="Usage Example", steps=4, emotional_bias=0.08)

    print("\n3. Resonance Between Two Agents (Resonate Examples)")
    agent1 = BaseAgent("HarmoniousOne", "test", emotional_state=0.75)
    agent2 = BaseAgent("DissonantOne", "test", emotional_state=-0.35)

    print(f"   Before resonance:\n     {agent1.id}: {agent1.emotional_state:.2f}\n     {agent2.id}: {agent2.emotional_state:.2f}")

    resonance_strength = agent1.resonate_with(agent2)
    print(f"   Resonance strength: {resonance_strength:.2f}")

    print(f"   After resonance:\n     {agent1.id}: {agent1.emotional_state:.2f}\n     {agent2.id}: {agent2.emotional_state:.2f}")

    print("\n4. Multiple Resonance Interactions (Emotional Contagion Over Time)")
    agent_a = BaseAgent("Optimist", "test", emotional_state=0.8)
    agent_b = BaseAgent("Pessimist", "test", emotional_state=-0.6)

    for i in range(3):
        res = agent_a.resonate_with(agent_b)
        print(f"   Step {i+1} - Resonance: {res:.2f} | Optimist: {agent_a.emotional_state:.2f}, Pessimist: {agent_b.emotional_state:.2f}")

    print("\n" + "=" * 70)
    print("All usage examples completed.")
    print("=" * 70)