import sys
import os
from collections import deque

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

_NEI8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def part_one(lines):
    grid = [list(line) for line in lines if line.strip()]
    if not grid:
        return 0
    h, w = len(grid), len(grid[0])
    count = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != "@":
                continue
            neighbors = 0
            for dr, dc in _NEI8:
                rr, cc = r + dr, c + dc
                if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == "@":
                    neighbors += 1
            if neighbors < 4:
                count += 1
    return count

def part_two(lines):
    grid = [list(line) for line in lines if line.strip()]
    if not grid:
        return 0
    h, w = len(grid), len(grid[0])

    alive = [[cell == "@" for cell in row] for row in grid]
    degree = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if not alive[r][c]:
                continue
            d = 0
            for dr, dc in _NEI8:
                rr, cc = r + dr, c + dc
                if 0 <= rr < h and 0 <= cc < w and alive[rr][cc]:
                    d += 1
            degree[r][c] = d

    q: deque[tuple[int, int]] = deque()
    for r in range(h):
        for c in range(w):
            if alive[r][c] and degree[r][c] < 4:
                q.append((r, c))

    removed = 0
    while q:
        r, c = q.popleft()
        if not alive[r][c]:
            continue
        if degree[r][c] >= 4:
            continue
        alive[r][c] = False
        removed += 1
        for dr, dc in _NEI8:
            rr, cc = r + dr, c + dc
            if 0 <= rr < h and 0 <= cc < w and alive[rr][cc]:
                degree[rr][cc] -= 1
                if degree[rr][cc] < 4:
                    q.append((rr, cc))
    return removed

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
