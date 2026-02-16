import random
from enum import Enum

class NodeType(Enum):
    INPUT = 0
    HIDDEN = 1
    OUTPUT = 2

class NodeGene:
    def __init__(self, node_id: int, node_type: NodeType):
        self.id = node_id
        self.type = node_type

    def copy(self):
        return NodeGene(self.id, self.type)

class ConnectionGene:
    def __init__(self, in_node: int, out_node: int, weight: float, enabled: bool, innovation: int):
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enabled = enabled
        self.innovation = innovation

    def copy(self):
        return ConnectionGene(self.in_node, self.out_node, self.weight, self.enabled, self.innovation)

class InnovationTracker:
    def __init__(self):
        self.current_innovation = 0
        self.history = {}  # (in_node, out_node) -> innovation_number

    def get_innovation(self, in_node: int, out_node: int) -> int:
        if (in_node, out_node) in self.history:
            return self.history[(in_node, out_node)]
        self.current_innovation += 1
        self.history[(in_node, out_node)] = self.current_innovation
        return self.current_innovation

class Genome:
    def __init__(self, inputs: int, outputs: int):
        self.nodes = {}  # node_id -> NodeGene
        self.connections = {}  # innovation -> ConnectionGene
        self.inputs = inputs
        self.outputs = outputs
        self.traits = {
            "size": 1.0,
            "metabolism": 1.0
        }

        # Initialize with input and output nodes
        for i in range(inputs):
            self.nodes[i] = NodeGene(i, NodeType.INPUT)
        for i in range(inputs, inputs + outputs):
            self.nodes[i] = NodeGene(i, NodeType.OUTPUT)

    def copy(self):
        new_genome = Genome(self.inputs, self.outputs)
        new_genome.nodes = {node_id: gene.copy() for node_id, gene in self.nodes.items()}
        new_genome.connections = {innov: gene.copy() for innov, gene in self.connections.items()}
        new_genome.traits = self.traits.copy()
        return new_genome

    def mutate_weights(self, power: float = 0.5):
        for conn in self.connections.values():
            if random.random() < 0.8:  # 80% chance to perturb
                conn.weight += random.uniform(-1, 1) * power
            else:  # 20% chance to assign new value
                conn.weight = random.uniform(-2, 2)

        # Mutate traits as well
        for trait in self.traits:
            self.traits[trait] *= random.uniform(0.9, 1.1)
            self.traits[trait] = max(0.1, min(5.0, self.traits[trait]))

    def mutate_add_connection(self, tracker: InnovationTracker):
        node_ids = list(self.nodes.keys())
        for _ in range(20):  # Try 20 times to find a valid connection
            in_node = random.choice(node_ids)
            out_node = random.choice(node_ids)

            # Rules:
            # 1. Not from output to anything
            # 2. Not from anything to input
            # 3. Not to itself
            # 4. Connection doesn't already exist
            if self.nodes[in_node].type == NodeType.OUTPUT: continue
            if self.nodes[out_node].type == NodeType.INPUT: continue
            if in_node == out_node: continue

            exists = any(c.in_node == in_node and c.out_node == out_node for c in self.connections.values())
            if not exists:
                innov = tracker.get_innovation(in_node, out_node)
                self.connections[innov] = ConnectionGene(in_node, out_node, random.uniform(-1, 1), True, innov)
                break

    def mutate_add_node(self, tracker: InnovationTracker):
        if not self.connections: return

        # Pick an enabled connection to split
        enabled_conns = [c for c in self.connections.values() if c.enabled]
        if not enabled_conns: return

        conn = random.choice(enabled_conns)
        conn.enabled = False

        new_node_id = len(self.nodes)
        self.nodes[new_node_id] = NodeGene(new_node_id, NodeType.HIDDEN)

        # in -> new (weight 1.0)
        innov1 = tracker.get_innovation(conn.in_node, new_node_id)
        self.connections[innov1] = ConnectionGene(conn.in_node, new_node_id, 1.0, True, innov1)

        # new -> out (weight of original conn)
        innov2 = tracker.get_innovation(new_node_id, conn.out_node)
        self.connections[innov2] = ConnectionGene(new_node_id, conn.out_node, conn.weight, True, innov2)

    @staticmethod
    def crossover(parent1: 'Genome', parent2: 'Genome') -> 'Genome':
        # Assume parent1 is the more fit one if needed, here we just combine
        # Actually in NEAT, the more fit parent's disjoint/excess genes are kept.
        # If equal fitness, we combine them.

        child = Genome(parent1.inputs, parent1.outputs)

        # Combine nodes
        for node_id, gene in parent1.nodes.items():
            child.nodes[node_id] = gene.copy()
        for node_id, gene in parent2.nodes.items():
            if node_id not in child.nodes:
                child.nodes[node_id] = gene.copy()

        # Combine connections
        all_innovs = set(parent1.connections.keys()).union(set(parent2.connections.keys()))
        for innov in all_innovs:
            if innov in parent1.connections and innov in parent2.connections:
                # If both have it, pick randomly
                gene = random.choice([parent1.connections[innov], parent2.connections[innov]])
                child.connections[innov] = gene.copy()
            elif innov in parent1.connections:
                child.connections[innov] = parent1.connections[innov].copy()
            # If only in parent2, and we assume parent1 is more fit, we ignore it.
            # But here we don't have fitness, so let's just take it if we want diversity.
            # In official NEAT, only genes from the more fit parent are taken if disjoint.
            # For simplicity, let's just take them all for now or pass fitness.
            elif innov in parent2.connections:
                child.connections[innov] = parent2.connections[innov].copy()

        # Combine traits
        for trait in child.traits:
            child.traits[trait] = (parent1.traits[trait] + parent2.traits[trait]) / 2

        return child

    def compatibility_distance(self, other: 'Genome') -> float:
        c1 = 1.0  # Coefficient for excess/disjoint genes
        c2 = 1.0
        c3 = 0.4  # Coefficient for weight difference

        innov1 = sorted(self.connections.keys())
        innov2 = sorted(other.connections.keys())

        if not innov1 and not innov2: return 0.0

        highest_innov1 = innov1[-1] if innov1 else 0
        highest_innov2 = innov2[-1] if innov2 else 0

        # Disjoint/Excess genes
        matching = 0
        disjoint = 0
        weight_diff = 0.0

        all_innovs = set(innov1).union(set(innov2))
        for innov in all_innovs:
            if innov in self.connections and innov in other.connections:
                matching += 1
                weight_diff += abs(self.connections[innov].weight - other.connections[innov].weight)
            else:
                disjoint += 1

        n = max(len(innov1), len(innov2))
        if n < 20: n = 1 # official NEAT suggests n=1 for small genomes

        distance = (c1 * disjoint) / n
        if matching > 0:
            distance += c3 * (weight_diff / matching)

        return distance

import math

def sigmoid(x):
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError:
        return 0 if x < 0 else 1

class NeuralNetwork:
    def __init__(self, genome: Genome):
        self.genome = genome
        # Pre-map node IDs to continuous indices for faster access
        self.node_ids = sorted(genome.nodes.keys())
        self.node_to_idx = {node_id: i for i, node_id in enumerate(self.node_ids)}
        self.num_nodes = len(self.node_ids)

        # Pre-allocate value buffers
        self.values = [0.0] * self.num_nodes
        self.new_values = [0.0] * self.num_nodes
        self._zeros = [0.0] * self.num_nodes

        # Pre-process enabled connections into indexed tuples
        self.indexed_connections = []
        for conn in genome.connections.values():
            if conn.enabled:
                self.indexed_connections.append((
                    self.node_to_idx[conn.in_node],
                    self.node_to_idx[conn.out_node],
                    conn.weight
                ))

        # Identify node categories by index
        self.input_indices = [self.node_to_idx[i] for i in range(genome.inputs)]
        self.output_indices = [self.node_to_idx[i] for i in range(genome.inputs, genome.inputs + genome.outputs)]

        # Non-input indices for sigmoid activation
        self.non_input_indices = [i for i, node_id in enumerate(self.node_ids)
                                 if genome.nodes[node_id].type != NodeType.INPUT]

    def activate(self, inputs: list[float]) -> list[float]:
        # Reset values
        self.values[:] = self._zeros

        # Set inputs
        for i, val in enumerate(inputs):
            if i < len(self.input_indices):
                self.values[self.input_indices[i]] = val

        # Simple iterative pass to handle hidden nodes and potential recurrence
        # We do multiple passes to let signals propagate
        for _ in range(3):
            # Reset new_values
            self.new_values[:] = self._zeros

            # Keep inputs constant
            for idx in self.input_indices:
                self.new_values[idx] = self.values[idx]

            # Accumulate signals
            for in_idx, out_idx, weight in self.indexed_connections:
                self.new_values[out_idx] += self.values[in_idx] * weight

            # Apply activation function
            for idx in self.non_input_indices:
                self.new_values[idx] = sigmoid(self.new_values[idx])

            # Swap buffers for next pass
            self.values, self.new_values = self.new_values, self.values

        # Collect outputs
        return [self.values[idx] for idx in self.output_indices]

global_innovation_tracker = InnovationTracker()
