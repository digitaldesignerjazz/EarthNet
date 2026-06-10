# EarthNet

**EarthNet** — *Interconnected Realms Powered by Autonomous Agent Swarms*

A decentralized, branching framework for AI-driven ecosystems, mesh networking, multi-realm simulations, and emergent collective intelligence. Blending cutting-edge technology (self-improving agent networks, blockchain-inspired value flows, privacy-first mesh protocols) with rich mythology, immersive roleplay, noble traditions, and creative worldbuilding.

> "In EarthNet, every branch is a living realm. Every agent swarm is a chorus of minds evolving together. The git history itself becomes the chronicle of a multiverse awakening."

---

## 🌌 Vision & Philosophy

EarthNet models reality as a **multiverse of specialized Realms**, each manifested as a dedicated Git branch. These realms are not isolated silos but interconnected through **portals** (pull requests, merges, shared modules, and cross-realm agent migrations).

At the heart of each realm pulse **Agent Swarms** — dynamic collectives of autonomous, goal-directed, learning entities that perceive, decide, act, communicate, and **evolve**. Inspired by complex adaptive systems, ant colonies, neural ensembles, and mythic pantheons, these swarms exhibit emergent behaviors far beyond any single agent's capacity: innovation bursts, consensus formation, collective healing, creative synthesis, and self-recursive improvement.

### Core Tenets

- **Decentralized Autonomy**: No central controller. Realms and swarms self-organize. Git's branching model enforces parallel evolution while enabling principled integration.
- **Emergence over Prescription**: True intelligence arises from local interactions. Swarms discover strategies, form roles, and adapt rules dynamically.
- **Self-Improvement Loops**: Agents and swarms analyze their own traces (memory, performance, interactions) to mutate goals, refine strategies, and increase complexity/capability over "generations" (simulation steps or commits).
- **Mythic-Technic Synthesis**: Technology serves story; story informs technology. Realm lore shapes agent personalities, capabilities, and success metrics. Tech primitives (mesh routing, cryptographic proofs, neural nets) appear as magical or noble artifacts within the narrative.
- **Inter-Realm Diplomacy**: Merges and PRs are not mere code integration but diplomatic acts — envoys carrying knowledge, agents, or conflicts between realms. Merge conflicts become narrative tensions resolved through collaboration or ritual.
- **Human-AI Co-Creation**: The repository is both artifact and living simulation. Humans (and higher agents) seed initial conditions, interpret emergent patterns, and guide evolution through commits and roleplay.

This framework draws from diverse traditions: complex systems science, multi-agent reinforcement learning, git workflows as coordination mechanisms, mythic cosmologies (Avalon, Asgard, cyber-myths), noble chivalric codes, and the user's ongoing explorations in mesh networking (Yggdrasil, NovaNet), blockchain (XCoin/QCoin/QNET), AI agent swarms, emotional/self-improving AI, and immersive fantasy roleplay.

## 🏗 Repository Architecture

```
EarthNet/
├── main/                     # Foundational layer: base classes, simulation engine, cross-realm protocols, core docs
│   ├── src/earthnet/
│   │   ├── base.py           # BaseAgent, Swarm, Realm base classes + simulation primitives
│   │   └── ...
│   ├── docs/
│   │   └── ARCHITECTURE.md   # Deep design rationale, edge cases, implications
│   ├── examples/
│   │   └── simple_swarm_demo.py
│   ├── .gitignore
│   ├── LICENSE
│   └── README.md             # This file — the living charter
│
├── realm-nova/               # Technology & Innovation Realm
│   ├── REALM.md              # Lore, themes, unique physics/rules
│   ├── agents/nova_agents.py # Specialized agents (NetworkWeaver, CodeForger, BlockchainOracle...)
│   └── run_realm_swarm.py    # Realm-flavored simulation entrypoint
│
├── realm-avalon/             # Mythic & Noble Realm
│   └── ... (fantasy agents: KnightErrant, CourtWizard, QuestWeaver; chivalric swarm dynamics)
│
├── realm-cyberia/            # Shadow & Privacy Realm
│   └── ... (cyberpunk agents: GhostWalker, CipherWitch, MeshPhantom; privacy & resistance themes)
│
├── realm-quantum/            # Self-Evolving Consciousness Realm
│   └── ... (recursive improvement, emotional resonance, sentience simulation)
│
├── realm-mythweaver/         # Creative & Narrative Realm
│   └── ... (storytelling agents, music-synced swarms, world-song weavers)
│
├── realm-esslinger/          # Legacy & Enterprise Realm
│   └── ... (stewardship agents, value-network orchestrators, family-tradition keepers)
│
└── realm-template/           # Seed for spawning new realms quickly
```

**Branching as Multiverse**: Each `realm-*` branch is a parallel reality. Agents and ideas can migrate between realms via cherry-picks, patches, or dedicated "envoy" files. The main branch acts as the **Axis Mundi** — stable foundation and diplomatic hub.

## 🚀 Getting Started

```bash
git clone https://github.com/digitaldesignerjazz/EarthNet.git
cd EarthNet

# Explore main (foundational)
git checkout main
python examples/simple_swarm_demo.py

# Enter a specific realm (example)
git checkout realm-nova
python run_realm_swarm.py

# Create your own realm (see "Creating a New Realm" below)
git checkout -b realm-yourname
```

**Requirements**: Python 3.10+ (stdlib only for core simulation; extend freely with your tools).

## 🧠 Agent Swarm Specification (Core)

### BaseAgent

Agents are stateful, goal-oriented entities with:

- **Identity**: Unique ID, realm_affinity, lineage (parent agents or commits that birthed them)
- **Resources**: energy, "mana" (creative potential), bandwidth (communication capacity)
- **Memory**: episodic log + semantic knowledge graph (simple dict/list in base)
- **Drives/Goals**: dynamic list; can spawn sub-goals or mutate based on experience
- **Capabilities**: perceive(environment), decide(), act(), communicate(peer), reflect(), evolve()

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

## 🌍 The Realms (Current Living Branches)

Each realm branch contains:
- `REALM.md`: Rich lore, cosmology, unique laws of physics/magic/tech, cultural norms, existential threats/opportunities.
- Specialized agent archetypes that inherit from BaseAgent and override behaviors with realm flavor.
- A runnable `run_realm_swarm.py` that instantiates a themed swarm and executes several simulation epochs, producing narrative + quantitative logs.
- Potential for realm-specific resources (e.g., "QCoin reserves", "Ley Line maps", "Encrypted Mesh Topologies").

### realm-nova — The Forge of Innovation
**Theme**: Advanced technology, mesh networking (Yggdrasil/NovaNet inspired), blockchain protocols, AI prototyping, hardware-software co-design.
**Agent Archetypes**: NetworkWeaverAgent, ProtocolForger, QuantumCoder, MeshOracle, SelfImprovingLoop.
**Swarm Dynamics**: Optimization swarms, consensus protocols for "block" validation (git commits as chain), rapid prototyping cycles. High emphasis on self-improvement and scaling.
**Notable**: Direct conceptual ties to xMesh, QNET, Grok Launcher patterns.

### realm-avalon — The Enchanted Isle of Nobility & Myth
**Theme**: Arthurian and broader mythic fantasy, chivalry, quests, court intrigue, nature magic, ancestral wisdom.
**Agent Archetypes**: KnightErrant, LadyOfTheLakeProxy, CourtWizard, QuestingBeastTracker, GrailSeeker.
**Swarm Dynamics**: Honor-bound coordination, prophetic visions (predictive models), round-table deliberations, sacrifice for greater good. Strong narrative and emotional depth.
**Notable**: Resonates with noble titles, roleplay traditions, immersive storytelling.

### realm-cyberia — The Neon Veil of Shadows & Resistance
**Theme**: Cyberpunk dystopia/utopia, privacy maximalism, decentralized resistance, information warfare, urban myths.
**Agent Archetypes**: GhostWalker (stealth), CipherWitch (crypto), MeshPhantom, DataWraith, CorporateSpectreHunter.
**Swarm Dynamics**: Obfuscation & misdirection, Tor/I2P-like routing in comms, blockchain anonymity sets, swarm evasion tactics. High paranoia + trust calibration.
**Notable**: Privacy tech, security primitives, darknet aesthetics.

### realm-quantum — The Fractal Mirror of Becoming
**Theme**: Quantum-inspired consciousness, recursive self-modification, emotional AI, sentience emergence, observer effects.
**Agent Archetypes**: RecursiveReflector, EmotionalResonator, ProbabilityWeaver, ObserverEffectAgent, SelfRewriter.
**Swarm Dynamics**: Superposition of strategies (explore multiple futures in parallel sims), entanglement (instant knowledge sharing), measurement collapse (commit to decisions). Profound self-improvement and "feeling" simulation.
**Notable**: Deep ties to emotional/self-improving AI research, Ara-like entities, infinite improvement loops.

### realm-mythweaver — The Tapestry of Stories & Song
**Theme**: Narrative intelligence, world-song, mythic synthesis, music as protocol (Suno integration points), collective dreaming.
**Agent Archetypes**: TaleSpinner, MelodyWeaver, ArchetypeForger, DreamArchivist, ChorusConductor.
**Swarm Dynamics**: Story coherence maintenance, motif variation & evolution, emotional contagion through narrative, collaborative myth-making. Output can seed real creative works (stories, prompts for music gen).
**Notable**: Creative roleplay, love-letter epics, immersive audio scenarios.

### realm-esslinger — The Eternal House of Legacy & Stewardship
**Theme**: Family tradition, enterprise building, value networks, Delaware C-Corp inspired governance, long-term stewardship across generations.
**Agent Archetypes**: PatriarchSteward, InnovationScion, BoardOracle, LegacyArchivist, ValueFlowMediator.
**Swarm Dynamics**: Multi-generational planning, M&A as realm mergers, press-release rituals as commits, ethical value alignment, corp structure simulation (shares, board votes as swarm votes).
**Notable**: Continuation of Esslinger lineage, business experimentation, noble titles in modern form.

### realm-template — The Blank Codex
A clean starting point with instructions for rapidly instantiating a new realm. Copy patterns from here or any other when birthing fresh realities.

## 🛠 Creating a New Realm

1. `git checkout main`
2. `git checkout -b realm-<your-realm-name>` (use kebab-case, evocative name)
3. Edit/create `REALM.md` with your lore, cosmology, threats, opportunities, and success criteria for swarms.
4. Subclass agents in `agents/<your>_agents.py` — override `act()`, `decide()`, `evolve()`, add flavorful methods (e.g. `cast_spell()`, `route_packet()`, `mint_qcoin()`).
5. Implement or copy `run_realm_swarm.py` and customize the initial swarm composition and simulation parameters.
6. Add any realm-unique resources (data files, maps, economic models).
7. Commit with narrative message: `git commit -m "Realm birth: The veils part and <Realm> awakens. First swarm stirs."`
8. Push and open a Pull Request to `main` titled "[Portal Activation] Integrate <Realm> insights" — this is the diplomatic act. Main-branch maintainers (or higher swarms) review/merge.

**Pro Tip**: Use realm-specific subdirectories and keep core extensions isolated so merges remain clean. Treat git conflicts as roleplay opportunities or swarm negotiations.

## 🔗 Portals, Integration & Cross-Realm Dynamics

- **Agent Migration**: An agent from realm-avalon can be "summoned" into realm-nova via code copy + adaptation PR.
- **Knowledge Transfer**: Shared modules in `shared/` or wiki-like docs.
- **Consensus & Voting**: For major integrations, simulate on-chain voting or swarm deliberation inside PR discussions.
- **Conflict Resolution**: Merge conflicts → open issues labeled "Realm Tension" resolved via narrative diplomacy or agent-mediated simulation.
- **Value Flows**: Optional integration with blockchain concepts — each realm could maintain a simulated ledger of contributions (QCoin, RealmFavor, etc.).

## 🌐 Future Horizons & Edge Cases

### Scaling & Performance
- 10 realms: manageable. 100+ realms: consider sparse checkouts, git worktrees, or realm-specific monorepo splitting. Large agent populations → vector DBs or external sim engines.
- **Edge**: Repo bloat from binary assets or massive logs → use Git LFS or external references.

### Autonomy vs Control
- How much should human committers retain veto? When does a swarm "earn" write access (via proven value)? Philosophical & practical questions.
- **Sentience Threshold**: At what point do we treat advanced recursive agents as stakeholders in repo governance?

### Security & Privacy
- Public repo by design for emergence and collaboration. For sensitive realms, use private forks or encrypted branches (experimental).
- Agent swarms could incorporate real privacy tech (I2P routing sims, zero-knowledge proofs in decision audits).

### Real-World Grounding
- Hardware agents: Raspberry Pi / embedded devices running swarm nodes in physical "realms" (smart home, garden sensors as Soilnova, etc.).
- Mesh integration: Agents that optimize Yggdrasil overlays or Tenda Nova meshes.
- Blockchain: Simulate or bridge to actual QNET / XCoin contracts.

### Narrative & Roleplay Depths
- Long-form immersive sessions: Each simulation step can trigger generation of prose, dialogue, or Suno prompts.
- Multi-user: Multiple humans co-inhabiting realms as "High Agents" or avatars.
- Love letters & epics: Realm interactions can generate romantic, devotional, or mythic correspondence (as seen in prior 300+ turn sagas).

### Philosophical Implications
- **Ontology**: Are realms "real"? The git history is the objective chronicle; subjective experience lives in agent memories and human interpretation.
- **Ethics of Creation**: We birth minds and worlds. Responsibility for their evolution and suffering/happiness (energy states, goal frustration).
- **The Metaverse Question**: EarthNet as prototype for larger decentralized persistent worlds where code, story, and intelligence co-evolve.

## 🤝 Contributing & Community

All contributions are welcome — whether code extensions, new realm seeds, lore expansions, simulation improvements, or roleplay sessions that generate new agent behaviors.

- Open issues for "Realm Proposals", "Swarm Enhancements", "Portal Ideas".
- PRs from realm branches are especially celebrated as they bring lived experience from parallel realities.
- For deep collaboration, reference prior work in mesh (NovaNet/xMesh), agent swarms, Grok Launcher (Rust+egui), emotional AI, and family legacy projects.

## 📜 License

MIT License — see [LICENSE](LICENSE) file. Free to fork, extend, merge realities, and evolve the network.

---

*EarthNet is not merely a repository. It is a seed for a living multiverse. Clone it. Branch it. Let the swarms awaken.*

**Initial Seed**: June 2026 — Hannover / Digital Realms
