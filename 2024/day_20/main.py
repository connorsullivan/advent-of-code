import sys
import os
from collections import deque

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_grid(lines):
    """Parse the grid and find start and end positions."""
    grid = [list(line) for line in lines]
    start = end = None

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    return grid, start, end

def bfs_distances(grid, start):
    """Calculate distances from start to all reachable positions using BFS."""
    rows, cols = len(grid), len(grid[0])
    distances = {}
    queue = deque([(start, 0)])
    distances[start] = 0

    while queue:
        (r, c), dist = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in distances:
                if grid[nr][nc] != '#':
                    distances[(nr, nc)] = dist + 1
                    queue.append(((nr, nc), dist + 1))

    return distances

def find_cheats(grid, start, end, max_cheat_time, min_savings):
    """Find all cheats that save at least min_savings picoseconds."""
    # Get distances from start to all positions
    distances_from_start = bfs_distances(grid, start)

    # Get distances from all positions to end by reversing (BFS from end)
    distances_from_end = bfs_distances(grid, end)

    # Normal path time without cheats
    normal_time = distances_from_start[end]

    cheats = {}

    # For each position on the normal path
    for pos1 in distances_from_start:
        r1, c1 = pos1
        dist_to_pos1 = distances_from_start[pos1]

        # Try all positions within Manhattan distance of max_cheat_time
        for dr in range(-max_cheat_time, max_cheat_time + 1):
            for dc in range(-max_cheat_time, max_cheat_time + 1):
                manhattan_dist = abs(dr) + abs(dc)
                if manhattan_dist == 0 or manhattan_dist > max_cheat_time:
                    continue

                r2, c2 = r1 + dr, c1 + dc
                pos2 = (r2, c2)

                # Check if pos2 is on the track
                if pos2 in distances_from_end:
                    # Calculate time with this cheat
                    time_with_cheat = dist_to_pos1 + manhattan_dist + distances_from_end[pos2]
                    savings = normal_time - time_with_cheat

                    if savings >= min_savings:
                        cheat_id = (pos1, pos2)
                        if cheat_id not in cheats or cheats[cheat_id] < savings:
                            cheats[cheat_id] = savings

    return len(cheats)

def part_one(lines):
    """Find cheats with max 2 picoseconds that save at least 100 picoseconds."""
    grid, start, end = parse_grid(lines)
    return find_cheats(grid, start, end, max_cheat_time=2, min_savings=100)

def part_two(lines):
    """Find cheats with max 20 picoseconds that save at least 100 picoseconds."""
    grid, start, end = parse_grid(lines)
    return find_cheats(grid, start, end, max_cheat_time=20, min_savings=100)

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
