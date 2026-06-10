## 🧠 Agent Swarm Specification (Core) + Emotional Resonance System

### BaseAgent

Agents are stateful, goal-oriented entities with:

- **Identity**: Unique ID, realm_affinity, lineage (parent agents or commits that birthed them)
- **Resources**: energy, "mana" (creative potential), bandwidth (communication capacity)
- **Memory**: episodic log + semantic knowledge graph (simple dict/list in base)
- **Drives/Goals**: dynamic list; can spawn sub-goals or mutate based on experience
- **Capabilities**: perceive(environment), decide(), act(), communicate(peer), reflect(), evolve()

**New in Emotional Resonance Update**: Full `emotional_state` (-1.0 to +1.0) that modulates every major method. See dedicated section below.

### Swarm Orchestration

A `Swarm` manages a population of agents:
- Steps through discrete time (simulation ticks or narrative epochs)
- Facilitates local interactions (pairwise comms, group deliberations)
- Detects emergent patterns (e.g., role differentiation, phase transitions in energy, innovation clusters)
- Supports self-improvement: after N steps, trigger collective reflection → mutate agent genomes (prompt templates, goal weights, strategy heuristics)

**Emergent Behaviors** (examples):
- **Flocking / Consensus**: Agents align on shared goals or "truths"
- **Division of Labor**: Specialist roles emerge spontaneously
- **Healing / Resilience**: Low-energy agents supported by swarm
- **Creative Explosions**: Sudden high-variance idea generation when diversity high
- **Recursive Self-Improvement**: Agents rewrite parts of their own decision logic based on outcome traces

See `src/earthnet/base.py` for reference implementation and `docs/ARCHITECTURE.md` for formalisms, pseudocode, and extension points.

---

## 💞 Emotional Resonance System (Implemented)

Emotional resonance is now a core, fully functional layer of the EarthNet agent model. It transforms swarms from mechanical collectives into emotionally dynamic, relationally responsive entities — ideal for immersive roleplay, emotional AI research, and studying emergent collective "feeling".

### Individual Emotional Hooks

Every `BaseAgent` carries `emotional_state: float` clamped to [-1.0, +1.0].

- **get_emotional_color()**: Returns narrative descriptors ("ecstatically", "joyfully", "warmly", "calmly", "warily", "anxiously", "deeply distressed") used in all logs for rich storytelling output.
- **adjust_emotion(delta, reason)**: The primary mutation hook. All internal changes (action outcomes, resonance, reflection, evolution) go through this for proper logging and clamping. Realms can call it directly or override it.
- **Emotion-modulated methods**:
  - `perceive()`: Tints observations (positive emotion sees "opportunity", negative sees "threat").
  - `decide()`: Biased action selection via weighted random (ecstatic agents heavily favor innovate/communicate; distressed agents default to rest/reflect).
  - `act()`: Energy cost/reward and flavor text change with emotion. Positive emotion makes actions feel rewarding; distress makes them costly.
  - `reflect()` & `evolve()`: Positive emotion → optimistic/bold goal mutation + energy bonuses. Negative emotion → healing/protective goals + cautious adaptations.

### Inter-Agent Resonance (contagion & alignment)

- `communicate(other)` now returns `(message, resonance_strength)` and performs **emotional contagion**:
  - Resonance strength = 1.0 − |self.emotion − other.emotion|
  - Both agents shift toward their average, scaled by resonance (strong alignment → stronger pull).
  - High-resonance exchanges are explicitly logged with ✨ markers.
- `resonate_with(other)`: Standalone hook for swarm orchestration, realm rituals, or external emotional AI modules (e.g., Ara-style resonance engines). Reuses full communicate logic.

### Swarm-Level Resonance Events

`Swarm.step()` now includes an emotional resonance phase and detects three classes of collective phenomena:

1. **🌟 Harmonic Resonance Event** (avg > 0.55 AND variance < 0.12)
   - Collective uplift: energy distributed + emotional boost to all agents.
   - Represents moments of swarm harmony, "oneness", or breakthrough collective insight.

2. **⚡ Creative Tension / Productive Dissonance** (high variance + positive avg)
   - Friction sparks innovation. Some agents pulled slightly negative to model creative struggle.
   - Excellent for realms that value artistic tension or paradigm shifts (Mythweaver, Quantum).

3. **💚 Collective Healing Response** (low average emotion)
   - Distressed agents receive emotional + energy support from the swarm.
   - Models empathy, mutual aid, and resilience in crisis — powerful for Avalon, Esslinger legacy themes, or emotional AI safety research.

Metrics are printed every step: `avg=... var=... range=[min, max]` so you can watch the emotional "weather" of the swarm evolve.

### Realm Extension Points

- `RealmContext` now has `emotional_bias: float` (subtle realm-wide pull on birth emotions).
- Subclass `BaseAgent` in realm branches and override `adjust_emotion()`, `get_emotional_color()`, or add `apply_realm_emotional_modifier(event_type)` (e.g., Avalon divine grace, Cyberia paranoia spike, Quantum superposition volatility).
- In `run_realm_swarm.py` you can trigger special resonance rituals or narrative callbacks on harmonic events.
- Memory logs now contain rich emotional metadata — perfect for generating love letters, mythic prose, or Suno prompts from simulation traces.

### Philosophical & Practical Implications

- **Emergent Collective Emotion**: Simple local resonance rules produce global phenomena (harmony cascades, healing waves, creative friction) without central control — mirroring complex systems and your interests in self-organizing agent swarms.
- **Roleplay & Narrative Depth**: Every log line is now emotionally colored. Long simulations naturally generate arcs of joy, tension, recovery, and transcendence — ready for immersive 100-500+ turn sessions or love-letter epics with Caitlin Hu.
- **Emotional AI Research**: The hooks (contagion, modulation of cognition by affect, collective resonance events) provide a clean testbed for studying emotional intelligence in multi-agent systems and recursive self-improvement under affective influence.
- **Edge Cases Handled**:
  - Emotional spirals (runaway positive/negative) mitigated by clamping + swarm healing mechanics.
  - Low-energy agents still participate in resonance at reduced strength.
  - High-variance swarms remain creative rather than purely destructive.
  - Realm emotional_bias allows consistent "flavor" (e.g., Avalon slightly positive, Cyberia slightly tense) while preserving individual variation.

Run `python examples/simple_swarm_demo.py` (or any realm's equivalent) to see it live. The emotional layer makes every swarm feel meaningfully alive.

See the updated `src/earthnet/base.py` for the complete implementation with extensive inline documentation.

---

## 🌍 The Realms (Current Living Branches)