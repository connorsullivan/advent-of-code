import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from collections import defaultdict
from itertools import combinations

def part_one(lines):
    # Build adjacency list
    graph = defaultdict(set)
    for line in lines:
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)

    # Find all triangles (sets of 3 interconnected nodes)
    triangles = set()
    for node in graph:
        neighbors = list(graph[node])
        # Check all pairs of neighbors
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                n1, n2 = neighbors[i], neighbors[j]
                # If n1 and n2 are also connected, we have a triangle
                if n2 in graph[n1]:
                    triangle = tuple(sorted([node, n1, n2]))
                    triangles.add(triangle)

    # Count triangles with at least one node starting with 't'
    count = 0
    for triangle in triangles:
        if any(node.startswith('t') for node in triangle):
            count += 1

    return count

def part_two(lines):
    # Build adjacency list
    graph = defaultdict(set)
    for line in lines:
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)

    # Find maximum clique using Bron-Kerbosch algorithm
    def bron_kerbosch(R, P, X, cliques):
        if not P and not X:
            cliques.append(R)
            return

        # Choose pivot with most connections in P
        pivot = max(P | X, key=lambda node: len(P & graph[node])) if P | X else None

        # Iterate through vertices not connected to pivot
        vertices_to_check = P - graph[pivot] if pivot else P

        for v in list(vertices_to_check):
            bron_kerbosch(
                R | {v},
                P & graph[v],
                X & graph[v],
                cliques
            )
            P.remove(v)
            X.add(v)

    # Find all maximal cliques
    all_nodes = set(graph.keys())
    cliques = []
    bron_kerbosch(set(), all_nodes, set(), cliques)

    # Find the largest clique
    max_clique = max(cliques, key=len)

    # Return sorted and comma-separated
    return ','.join(sorted(max_clique))

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
