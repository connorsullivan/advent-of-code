import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

from collections import defaultdict

def parse_graph(lines):
    adj = defaultdict(set)
    for line in lines:
        if not line.strip():
            continue
        u, v = line.strip().split('-')
        adj[u].add(v)
        adj[v].add(u)
    return adj

def part_one(lines):
    adj = parse_graph(lines)
    triangles = set()

    nodes = sorted(adj.keys())
    for i, u in enumerate(nodes):
        for v in adj[u]:
            if v > u:
                common = adj[u].intersection(adj[v])
                for w in common:
                    if w > v:
                        triangles.add((u, v, w))

    count = 0
    for tri in triangles:
        if any(node.startswith('t') for node in tri):
            count += 1

    return count

def part_two(lines):
    adj = parse_graph(lines)

    max_clique = []

    def bron_kerbosch(r, p, x):
        nonlocal max_clique

        # Pruning: if current clique size + potential candidates <= max found so far, stop
        if len(r) + len(p) <= len(max_clique):
            return

        if not p and not x:
            if len(r) > len(max_clique):
                max_clique = list(r)
            return

        # Pivot selection
        # Choose pivot u in P U X that maximizes |P intersect N(u)|
        pivot_candidates = p.union(x)
        if not pivot_candidates:
            return

        pivot = max(pivot_candidates, key=lambda u: len(p.intersection(adj[u])))

        # Iterate over candidates in P that are NOT neighbors of pivot
        for v in p.difference(adj[pivot]):
            bron_kerbosch(r.union({v}), p.intersection(adj[v]), x.intersection(adj[v]))
            p.remove(v)
            x.add(v)

    bron_kerbosch(set(), set(adj.keys()), set())

    return ",".join(sorted(max_clique))

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
