import sys
import os
from collections import deque

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_bytes(lines):
    """Parse byte coordinates from input lines."""
    bytes_list = []
    for line in lines:
        if line.strip():
            x, y = map(int, line.strip().split(','))
            bytes_list.append((x, y))
    return bytes_list

def bfs_shortest_path(corrupted, grid_size):
    """Find shortest path from (0,0) to (grid_size-1, grid_size-1) using BFS."""
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    if start in corrupted or end in corrupted:
        return -1

    queue = deque([(start, 0)])  # (position, steps)
    visited = {start}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < grid_size and
                0 <= ny < grid_size and
                (nx, ny) not in corrupted and
                (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1  # No path found

def part_one(lines, num_bytes=1024, grid_size=71):
    """Find shortest path after num_bytes have fallen."""
    bytes_list = parse_bytes(lines)

    # Simulate first num_bytes falling
    corrupted = set(bytes_list[:num_bytes])

    return bfs_shortest_path(corrupted, grid_size)

def part_two(lines, grid_size=71):
    """Find first byte that blocks the path completely."""
    bytes_list = parse_bytes(lines)

    # Binary search approach: find first byte where path becomes impossible
    # We know path exists at start, and doesn't exist at end
    left, right = 0, len(bytes_list) - 1
    result_idx = -1

    while left <= right:
        mid = (left + right) // 2
        corrupted = set(bytes_list[:mid + 1])

        if bfs_shortest_path(corrupted, grid_size) == -1:
            # Path blocked at mid, try earlier
            result_idx = mid
            right = mid - 1
        else:
            # Path still exists, try later
            left = mid + 1

    if result_idx != -1:
        x, y = bytes_list[result_idx]
        return f"{x},{y}"

    return None

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
