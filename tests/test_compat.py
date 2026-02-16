import sys
import os
sys.path.append(os.getcwd())

from neat_core import Genome, global_innovation_tracker, ConnectionGene

def test_compatibility_distance():
    g1 = Genome(2, 1)
    g2 = Genome(2, 1)

    # Matching gene
    innov1 = global_innovation_tracker.get_innovation(0, 2)
    g1.connections[innov1] = ConnectionGene(0, 2, 1.0, True, innov1)
    g2.connections[innov1] = ConnectionGene(0, 2, 0.5, True, innov1)

    # Disjoint gene in g1
    innov2 = global_innovation_tracker.get_innovation(1, 2)
    g1.connections[innov2] = ConnectionGene(1, 2, 1.0, True, innov2)

    # d = (c1 * disjoint) / n + c3 * weight_diff / matching
    # disjoint = 1 (innov2 only in g1)
    # matching = 1 (innov1)
    # weight_diff = |1.0 - 0.5| = 0.5
    # n = max(len(g1), len(g2)) = 2
    # Since n < 20, n becomes 1 in the current code
    # d = (1.0 * 1) / 1 + 0.4 * (0.5 / 1) = 1.0 + 0.2 = 1.2

    dist = g1.compatibility_distance(g2)
    assert abs(dist - 1.2) < 1e-6

    # Test identical genomes
    assert g1.compatibility_distance(g1) == 0.0

    # Test empty genomes
    g3 = Genome(2, 1)
    g4 = Genome(2, 1)
    assert g3.compatibility_distance(g4) == 0.0

if __name__ == "__main__":
    test_compatibility_distance()
    print("Test passed!")
