import sys
import os
sys.path.append(os.getcwd())

from neat_core import Genome, global_innovation_tracker, NeuralNetwork, NodeType

def test_genome_mutation():
    g = Genome(2, 1)
    assert len(g.nodes) == 3
    assert len(g.connections) == 0

    g.mutate_add_connection(global_innovation_tracker)
    assert len(g.connections) == 1

    g.mutate_add_node(global_innovation_tracker)
    assert len(g.nodes) == 4
    # Split one conn into two
    assert len(g.connections) == 3

def test_crossover():
    g1 = Genome(2, 1)
    g2 = Genome(2, 1)

    g1.mutate_add_connection(global_innovation_tracker)
    g2.mutate_add_connection(global_innovation_tracker)

    child = Genome.crossover(g1, g2)
    assert child.inputs == 2
    assert child.outputs == 1
    assert len(child.nodes) >= 3

def test_neural_network():
    g = Genome(2, 1)
    # Connect input 0 to output 2
    innov = global_innovation_tracker.get_innovation(0, 2)
    # Manual assignment to avoid randomness in test
    from neat_core import ConnectionGene
    g.connections[innov] = ConnectionGene(0, 2, 1.0, True, innov)

    nn = NeuralNetwork(g)
    out = nn.activate([1.0, 0.0])
    assert len(out) == 1
    # sigmoid(1.0 * 1.0) approx 0.731
    assert 0.7 < out[0] < 0.8

if __name__ == "__main__":
    test_genome_mutation()
    test_crossover()
    test_neural_network()
    print("All tests passed!")
