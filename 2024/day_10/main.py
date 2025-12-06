import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    grid = [[int(c) for c in line] for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    trailheads = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                trailheads.append((r, c))

    total_score = 0

    for start_r, start_c in trailheads:
        # BFS to find reachable 9s
        queue = [(start_r, start_c)]
        visited = set([(start_r, start_c)])
        reachable_nines = set()

        while queue:
            r, c = queue.pop(0)

            if grid[r][c] == 9:
                reachable_nines.add((r, c))
                continue

            current_height = grid[r][c]

            # Check neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited:
                        if grid[nr][nc] == current_height + 1:
                            visited.add((nr, nc))
                            queue.append((nr, nc))

        total_score += len(reachable_nines)

    return total_score

def part_two(lines):
    grid = [[int(c) for c in line] for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    memo = {}

    def count_paths(r, c):
        if (r, c) in memo:
            return memo[(r, c)]

        if grid[r][c] == 9:
            return 1

        total_paths = 0
        current_height = grid[r][c]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == current_height + 1:
                    total_paths += count_paths(nr, nc)

        memo[(r, c)] = total_paths
        return total_paths

    total_rating = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_rating += count_paths(r, c)

    return total_rating

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
