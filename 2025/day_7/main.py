import sys
import os
from collections import deque

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _find_start(grid: list[str]) -> tuple[int, int]:
    for r, row in enumerate(grid):
        c = row.find("S")
        if c != -1:
            return r, c
    raise ValueError("Missing start 'S'")


def part_one(lines):
    grid = [line for line in lines if line]
    if not grid:
        return 0
    h, w = len(grid), len(grid[0])
    _, sx = _find_start(grid)

    positions = {sx}
    splits = 0
    for r in range(1, h):
        next_positions = {x for x in positions if 0 <= x < w}
        q: deque[int] = deque([x for x in next_positions if grid[r][x] == "^"])
        while q:
            x = q.popleft()
            if x not in next_positions or grid[r][x] != "^":
                continue
            next_positions.remove(x)
            splits += 1
            for nx in (x - 1, x + 1):
                if 0 <= nx < w:
                    if nx not in next_positions:
                        next_positions.add(nx)
                        if grid[r][nx] == "^":
                            q.append(nx)
        positions = next_positions
    return splits

def part_two(lines):
    grid = [line for line in lines if line]
    if not grid:
        return 0
    h, w = len(grid), len(grid[0])
    _, sx = _find_start(grid)

    counts: dict[int, int] = {sx: 1}
    for r in range(1, h):
        next_counts: dict[int, int] = {}
        for x, c in counts.items():
            if 0 <= x < w:
                next_counts[x] = next_counts.get(x, 0) + c

        q: deque[int] = deque([x for x in next_counts if grid[r][x] == "^"])
        while q:
            x = q.popleft()
            c = next_counts.get(x, 0)
            if not c or grid[r][x] != "^":
                continue
            next_counts.pop(x, None)
            for nx in (x - 1, x + 1):
                if 0 <= nx < w:
                    next_counts[nx] = next_counts.get(nx, 0) + c
                    if grid[r][nx] == "^":
                        q.append(nx)
        counts = next_counts
    return sum(counts.values())

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
