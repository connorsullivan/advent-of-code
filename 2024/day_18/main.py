import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from collections import deque

def solve_maze(corrupted, width, height):
    start = (0, 0)
    end = (width, height)

    if start in corrupted or end in corrupted:
        return -1

    queue = deque([(start, 0)])
    visited = {start}

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx <= width and 0 <= ny <= height:
                if (nx, ny) not in corrupted and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

    return -1

def part_one(lines):
    coords = []
    for line in lines:
        x, y = map(int, line.strip().split(','))
        coords.append((x, y))

    # Simulate first 1024 bytes
    corrupted = set(coords[:1024])

    # Grid size is 0 to 70, so width and height are 70
    return solve_maze(corrupted, 70, 70)

def part_two(lines):
    coords = []
    for line in lines:
        x, y = map(int, line.strip().split(','))
        coords.append((x, y))

    width, height = 70, 70

    # Binary search for the first byte that blocks the path
    low = 1024
    high = len(coords) - 1
    first_blocking_index = -1

    while low <= high:
        mid = (low + high) // 2
        corrupted = set(coords[:mid+1])

        if solve_maze(corrupted, width, height) == -1:
            first_blocking_index = mid
            high = mid - 1
        else:
            low = mid + 1

    if first_blocking_index != -1:
        x, y = coords[first_blocking_index]
        return f"{x},{y}"

    return None

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
