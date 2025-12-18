import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Connect 1000 closest pairs and find product of 3 largest circuits."""
    import math
    
    # Parse junction box positions
    boxes = []
    for line in lines:
        coords = line.split(',')
        boxes.append((int(coords[0]), int(coords[1]), int(coords[2])))
    
    n = len(boxes)
    
    # Calculate all pairwise distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt(
                (boxes[i][0] - boxes[j][0]) ** 2 +
                (boxes[i][1] - boxes[j][1]) ** 2 +
                (boxes[i][2] - boxes[j][2]) ** 2
            )
            edges.append((dist, i, j))
    
    # Sort by distance
    edges.sort()
    
    # Union-Find
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # Try to connect 1000 closest pairs (some may already be connected)
    attempts = 0
    for dist, i, j in edges:
        if attempts >= 1000:
            break
        attempts += 1
        union(i, j)  # Try to connect (may not do anything if already connected)
    
    # Count circuit sizes
    circuits = {}
    for i in range(n):
        root = find(i)
        circuits[root] = circuits.get(root, 0) + 1
    
    # Get three largest
    sizes = sorted(circuits.values(), reverse=True)
    if len(sizes) < 3:
        return 0
    return sizes[0] * sizes[1] * sizes[2]

def part_two(lines):
    """Connect until all in one circuit, return X1 * X2 of last connection."""
    import math
    
    # Parse junction box positions
    boxes = []
    for line in lines:
        coords = line.split(',')
        boxes.append((int(coords[0]), int(coords[1]), int(coords[2])))
    
    n = len(boxes)
    
    # Calculate all pairwise distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt(
                (boxes[i][0] - boxes[j][0]) ** 2 +
                (boxes[i][1] - boxes[j][1]) ** 2 +
                (boxes[i][2] - boxes[j][2]) ** 2
            )
            edges.append((dist, i, j))
    
    # Sort by distance
    edges.sort()
    
    # Union-Find
    parent = list(range(n))
    num_components = n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        nonlocal num_components
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            num_components -= 1
            return True
        return False
    
    # Connect until all in one circuit
    last_i, last_j = -1, -1
    for dist, i, j in edges:
        if union(i, j):
            last_i, last_j = i, j
            if num_components == 1:
                break
    
    # Return product of X coordinates
    return boxes[last_i][0] * boxes[last_j][0]

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
