import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def find_guard_and_obstacles(lines):
    """Find the guard's starting position and all obstacles."""
    guard_pos = None
    guard_dir = None
    obstacles = set()

    direction_map = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.add((x, y))
            elif char in direction_map:
                guard_pos = (x, y)
                guard_dir = direction_map[char]

    return guard_pos, guard_dir, obstacles

def turn_right(direction):
    """Turn right 90 degrees."""
    dx, dy = direction
    return (-dy, dx)

def simulate_guard(lines, extra_obstacle=None):
    """
    Simulate the guard's movement.
    Returns (visited_positions, is_loop).
    """
    guard_pos, guard_dir, obstacles = find_guard_and_obstacles(lines)

    if extra_obstacle:
        obstacles = obstacles.copy()
        obstacles.add(extra_obstacle)

    height = len(lines)
    width = len(lines[0]) if lines else 0

    visited = {guard_pos}
    # Track states (position + direction) to detect loops
    states = {(guard_pos, guard_dir)}

    while True:
        x, y = guard_pos
        dx, dy = guard_dir
        next_pos = (x + dx, y + dy)

        # Check if guard would leave the area
        if next_pos[0] < 0 or next_pos[0] >= width or next_pos[1] < 0 or next_pos[1] >= height:
            return visited, False

        # Check if there's an obstacle ahead
        if next_pos in obstacles:
            # Turn right
            guard_dir = turn_right(guard_dir)
        else:
            # Move forward
            guard_pos = next_pos
            visited.add(guard_pos)

            # Check for loop
            state = (guard_pos, guard_dir)
            if state in states:
                return visited, True
            states.add(state)

def part_one(lines):
    """Count distinct positions visited by the guard."""
    visited, _ = simulate_guard(lines)
    return len(visited)

def part_two(lines):
    """
    Count positions where placing an obstacle would create a loop.
    """
    # First, get the guard's original path
    guard_start, _, obstacles = find_guard_and_obstacles(lines)
    original_visited, _ = simulate_guard(lines)

    # Only test positions that are in the original path (excluding start)
    # This optimization significantly reduces the search space
    candidates = original_visited - {guard_start}

    loop_positions = 0

    for pos in candidates:
        if pos not in obstacles:  # Can't place obstacle where one exists
            _, is_loop = simulate_guard(lines, extra_obstacle=pos)
            if is_loop:
                loop_positions += 1

    return loop_positions

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
