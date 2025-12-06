import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def get_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    path = [start]
    visited = {start}
    current = start

    while current != end:
        r, c = current
        found_next = False
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                path.append((nr, nc))
                current = (nr, nc)
                found_next = True
                break
        if not found_next:
            break

    return path

def solve(lines, max_cheat_dist):
    grid = [list(line) for line in lines]
    path = get_path(grid)
    dist = {pos: i for i, pos in enumerate(path)}
    count = 0

    for i, (r, c) in enumerate(path):
        for dr in range(-max_cheat_dist, max_cheat_dist + 1):
            for dc in range(-(max_cheat_dist - abs(dr)), (max_cheat_dist - abs(dr)) + 1):
                nr, nc = r + dr, c + dc
                if (nr, nc) in dist:
                    j = dist[(nr, nc)]
                    if j > i:
                        d = abs(dr) + abs(dc)
                        saved = j - i - d
                        if saved >= 100:
                            count += 1
    return count

def part_one(lines):
    return solve(lines, 2)

def part_two(lines):
    return solve(lines, 20)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
