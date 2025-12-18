import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

DELTAS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def build_grid(lines):
    return [[ch == "@" for ch in line] for line in lines]

def neighbor_counts(grid):
    rows, cols = len(grid), len(grid[0])
    counts = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if not grid[r][c]:
                continue
            for dr, dc in DELTAS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                    counts[r][c] += 1
    return counts

def part_one(lines):
    grid = build_grid(lines)
    counts = neighbor_counts(grid)
    accessible = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] and counts[r][c] < 4:
                accessible += 1
    return accessible

def part_two(lines):
    from collections import deque

    grid = build_grid(lines)
    counts = neighbor_counts(grid)
    rows, cols = len(grid), len(grid[0])
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] and counts[r][c] < 4:
                q.append((r, c))
    removed = 0
    while q:
        r, c = q.popleft()
        if not grid[r][c]:
            continue
        grid[r][c] = False
        removed += 1
        for dr, dc in DELTAS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                counts[nr][nc] -= 1
                if counts[nr][nc] < 4:
                    q.append((nr, nc))
    return removed

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
