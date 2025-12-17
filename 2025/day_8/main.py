import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.num_components -= 1
            return True
        return False

    def get_sizes(self):
        sizes = []
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                sizes.append(self.size[i])
        return sizes

def get_pairs(coords):
    n = len(coords)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = coords[i][0] - coords[j][0]
            dy = coords[i][1] - coords[j][1]
            dz = coords[i][2] - coords[j][2]
            dist_sq = dx*dx + dy*dy + dz*dz
            pairs.append((dist_sq, i, j))
    pairs.sort()
    return pairs

def part_one(lines):
    coords = []
    for line in lines:
        if not line.strip(): continue
        coords.append(list(map(int, line.split(','))))

    n = len(coords)
    pairs = get_pairs(coords)

    uf = UnionFind(n)
    for k in range(min(1000, len(pairs))):
        dist_sq, i, j = pairs[k]
        uf.union(i, j)

    sizes = sorted(uf.get_sizes(), reverse=True)
    if len(sizes) < 3:
        return 0 # Should not happen based on problem description
    return sizes[0] * sizes[1] * sizes[2]

def part_two(lines):
    coords = []
    for line in lines:
        if not line.strip(): continue
        coords.append(list(map(int, line.split(','))))

    n = len(coords)
    pairs = get_pairs(coords)

    uf = UnionFind(n)
    last_pair = None
    for dist_sq, i, j in pairs:
        if uf.union(i, j):
            last_pair = (i, j)
            if uf.num_components == 1:
                break

    if last_pair:
        return coords[last_pair[0]][0] * coords[last_pair[1]][0]
    return 0

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
