import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Find the sum of scores of all trailheads.
    Score = number of unique 9-height positions reachable from a trailhead."""
    grid = [[int(c) for c in line.strip()] for line in lines if line.strip()]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def bfs_reachable_nines(start_r, start_c):
        """Find all 9s reachable from a trailhead using BFS."""
        visited = set()
        reachable_nines = set()
        queue = [(start_r, start_c)]
        visited.add((start_r, start_c))

        while queue:
            r, c = queue.pop(0)
            current_height = grid[r][c]

            if current_height == 9:
                reachable_nines.add((r, c))
                continue

            # Check all 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if grid[nr][nc] == current_height + 1:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return len(reachable_nines)

    # Find all trailheads (height 0) and calculate their scores
    total_score = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                score = bfs_reachable_nines(r, c)
                total_score += score

    return total_score

def part_two(lines):
    """Find the sum of ratings of all trailheads.
    Rating = number of distinct hiking trails from a trailhead to any 9."""
    grid = [[int(c) for c in line.strip()] for line in lines if line.strip()]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def count_distinct_trails(r, c, target_height=9):
        """Count all distinct paths from (r,c) to any position with target_height."""
        current_height = grid[r][c]

        # Base case: reached a 9
        if current_height == target_height:
            return 1

        # Count trails through all valid neighbors
        trail_count = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == current_height + 1:
                    trail_count += count_distinct_trails(nr, nc, target_height)

        return trail_count

    # Find all trailheads (height 0) and calculate their ratings
    total_rating = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                rating = count_distinct_trails(r, c)
                total_rating += rating

    return total_rating

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
