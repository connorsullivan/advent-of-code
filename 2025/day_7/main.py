import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    grid = lines
    rows, cols = len(grid), len(grid[0])
    splitters = {}
    start_col = None
    start_row = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "^":
                splitters.setdefault(c, []).append(r)
            elif ch == "S":
                start_row, start_col = r, c
    for col in splitters:
        splitters[col].sort()

    from bisect import bisect_left
    memo = {}

    def next_split(col, r):
        lst = splitters.get(col, [])
        idx = bisect_left(lst, r)
        if idx == len(lst):
            return None
        return lst[idx]

    def dfs(col, r):
        if col < 0 or col >= cols:
            return 0
        key = (col, r)
        if key in memo:
            return memo[key]
        ns = next_split(col, r)
        if ns is None:
            memo[key] = 0
            return 0
        result = 1 + dfs(col - 1, ns) + dfs(col + 1, ns)
        memo[key] = result
        return result

    return dfs(start_col, start_row + 1)

def part_two(lines):
    grid = lines
    rows, cols = len(grid), len(grid[0])
    splitters = {}
    start_col = None
    start_row = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "^":
                splitters.setdefault(c, []).append(r)
            elif ch == "S":
                start_row, start_col = r, c
    for col in splitters:
        splitters[col].sort()

    from bisect import bisect_left
    memo = {}

    def next_split(col, r):
        lst = splitters.get(col, [])
        idx = bisect_left(lst, r)
        if idx == len(lst):
            return None
        return lst[idx]

    def timelines(col, r):
        if col < 0 or col >= cols:
            return 1
        key = (col, r)
        if key in memo:
            return memo[key]
        ns = next_split(col, r)
        if ns is None:
            memo[key] = 1
            return 1
        result = timelines(col - 1, ns) + timelines(col + 1, ns)
        memo[key] = result
        return result

    return timelines(start_col, start_row + 1)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
