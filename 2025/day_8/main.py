import sys
import os
from dataclasses import dataclass

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input


@dataclass
class DSU:
    parent: list[int]
    size: list[int]
    components: int

    @classmethod
    def create(cls, n: int) -> "DSU":
        return cls(parent=list(range(n)), size=[1] * n, components=n)

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def _parse_points(lines: list[str]) -> list[tuple[int, int, int]]:
    pts: list[tuple[int, int, int]] = []
    for line in lines:
        if not line:
            continue
        x, y, z = (int(p) for p in line.split(","))
        pts.append((x, y, z))
    return pts


def _edges(points: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    edges: list[tuple[int, int, int]] = []
    n = len(points)
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            edges.append((d2, i, j))
    edges.sort()
    return edges


def part_one(lines):
    points = _parse_points(lines)
    edges = _edges(points)
    dsu = DSU.create(len(points))
    for _, i, j in edges[:1000]:
        dsu.union(i, j)
    sizes = []
    seen = set()
    for i in range(len(points)):
        r = dsu.find(i)
        if r not in seen:
            seen.add(r)
            sizes.append(dsu.size[r])
    sizes.sort(reverse=True)
    while len(sizes) < 3:
        sizes.append(1)
    return sizes[0] * sizes[1] * sizes[2]

def part_two(lines):
    points = _parse_points(lines)
    edges = _edges(points)
    dsu = DSU.create(len(points))
    last_i = last_j = None
    for _, i, j in edges:
        if dsu.union(i, j):
            last_i, last_j = i, j
            if dsu.components == 1:
                break
    if last_i is None or last_j is None:
        return 0
    return points[last_i][0] * points[last_j][0]

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
