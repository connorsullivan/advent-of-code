import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    # Find start position
    start_pos = None
    direction = 0 # 0: Up, 1: Right, 2: Down, 3: Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '^':
                start_pos = (r, c)
                break
        if start_pos:
            break

    visited = set()
    visited.add(start_pos)

    curr_r, curr_c = start_pos
    curr_dir = direction

    while True:
        dr, dc = directions[curr_dir]
        next_r, next_c = curr_r + dr, curr_c + dc

        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        if grid[next_r][next_c] == '#':
            curr_dir = (curr_dir + 1) % 4
        else:
            curr_r, curr_c = next_r, next_c
            visited.add((curr_r, curr_c))

    return len(visited)

def part_two(lines):
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    start_pos = None
    direction = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '^':
                start_pos = (r, c)
                break
        if start_pos:
            break

    # Get original path to find candidates
    visited_path = set()
    curr_r, curr_c = start_pos
    curr_dir = direction

    while True:
        visited_path.add((curr_r, curr_c))
        dr, dc = directions[curr_dir]
        next_r, next_c = curr_r + dr, curr_c + dc

        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        if grid[next_r][next_c] == '#':
            curr_dir = (curr_dir + 1) % 4
        else:
            curr_r, curr_c = next_r, next_c

    candidates = visited_path - {start_pos}
    loop_count = 0

    for cr, cc in candidates:
        grid[cr][cc] = '#'

        # Simulate
        curr_r, curr_c = start_pos
        curr_dir = 0
        states = set()
        is_loop = False

        while True:
            state = (curr_r, curr_c, curr_dir)
            if state in states:
                is_loop = True
                break
            states.add(state)

            dr, dc = directions[curr_dir]
            next_r, next_c = curr_r + dr, curr_c + dc

            if not (0 <= next_r < rows and 0 <= next_c < cols):
                break

            if grid[next_r][next_c] == '#':
                curr_dir = (curr_dir + 1) % 4
            else:
                curr_r, curr_c = next_r, next_c

        if is_loop:
            loop_count += 1

        grid[cr][cc] = '.'

    return loop_count

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
