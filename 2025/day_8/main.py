import sys
import os
import math

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    """Parse junction box coordinates."""
    boxes = []
    for line in lines:
        if line:
            x, y, z = map(int, line.split(','))
            boxes.append((x, y, z))
    return boxes

def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
    
    def get_size(self, x):
        return self.size[self.find(x)]

def part_one(lines):
    """Connect 1000 closest pairs and multiply sizes of 3 largest circuits."""
    boxes = parse_input(lines)
    n = len(boxes)
    
    # Generate all pairs with distances
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(boxes[i], boxes[j])
            pairs.append((d, i, j))
    
    # Sort by distance
    pairs.sort()
    
    # Connect 1000 closest pairs
    uf = UnionFind(n)
    connections = 0
    for d, i, j in pairs:
        if connections >= 1000:
            break
        uf.union(i, j)
        connections += 1
    
    # Find circuit sizes
    circuit_sizes = {}
    for i in range(n):
        root = uf.find(i)
        circuit_sizes[root] = uf.get_size(i)
    
    sizes = sorted(circuit_sizes.values(), reverse=True)
    
    # Multiply 3 largest
    return sizes[0] * sizes[1] * sizes[2] if len(sizes) >= 3 else 0

def part_two(lines):
    """Find X coordinates of last two boxes to connect to form single circuit."""
    boxes = parse_input(lines)
    n = len(boxes)
    
    # Generate all pairs with distances
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(boxes[i], boxes[j])
            pairs.append((d, i, j))
    
    # Sort by distance
    pairs.sort()
    
    # Connect until all in same circuit
    uf = UnionFind(n)
    last_pair = None
    
    for d, i, j in pairs:
        if uf.union(i, j):
            # Check if all now in same circuit
            root = uf.find(0)
            if uf.get_size(root) == n:
                last_pair = (i, j)
                break
    
    if last_pair:
        return boxes[last_pair[0]][0] * boxes[last_pair[1]][0]
    return 0

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
