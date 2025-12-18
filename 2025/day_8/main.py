import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    points = [tuple(map(int, line.split(","))) for line in lines]
    n = len(points)
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            edges.append((dist, i, j))
    edges.sort()

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    for idx, (_, a, b) in enumerate(edges[:1000]):
        union(a, b)

    comp_sizes = {}
    for i in range(n):
        r = find(i)
        comp_sizes[r] = comp_sizes.get(r, 0) + 1
    largest = sorted(comp_sizes.values(), reverse=True)[:3]
    while len(largest) < 3:
        largest.append(1)
    return largest[0] * largest[1] * largest[2]

def part_two(lines):
    points = [tuple(map(int, line.split(","))) for line in lines]
    n = len(points)
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            edges.append((dist, i, j))
    edges.sort()

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    components = n
    last_pair = None
    for _, a, b in edges:
        merged = union(a, b)
        if merged:
            components -= 1
            if components == 1:
                last_pair = (a, b)
                break
    if last_pair is None:
        return 0
    x1, _, _ = points[last_pair[0]]
    x2, _, _ = points[last_pair[1]]
    return x1 * x2

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
