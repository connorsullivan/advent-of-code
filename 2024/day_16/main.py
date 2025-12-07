import sys
import os
import heapq
from collections import defaultdict

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Find the lowest score to reach the end tile."""
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])

    # Find start and end positions
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    # Directions: 0=East, 1=South, 2=West, 3=North
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Priority queue: (score, row, col, direction)
    # Start facing East (direction 0)
    pq = [(0, start[0], start[1], 0)]
    visited = {}

    while pq:
        score, r, c, d = heapq.heappop(pq)

        # If we reached the end, return the score
        if (r, c) == end:
            return score

        # Skip if we've visited this state with a better score
        state = (r, c, d)
        if state in visited:
            continue
        visited[state] = score

        # Try moving forward
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            new_state = (nr, nc, d)
            if new_state not in visited:
                heapq.heappush(pq, (score + 1, nr, nc, d))

        # Try rotating clockwise
        new_d = (d + 1) % 4
        new_state = (r, c, new_d)
        if new_state not in visited:
            heapq.heappush(pq, (score + 1000, r, c, new_d))

        # Try rotating counterclockwise
        new_d = (d - 1) % 4
        new_state = (r, c, new_d)
        if new_state not in visited:
            heapq.heappush(pq, (score + 1000, r, c, new_d))

    return None

def part_two(lines):
    """Count tiles that are part of at least one best path."""
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])

    # Find start and end positions
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    # Directions: 0=East, 1=South, 2=West, 3=North
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # First pass: find minimum score to each state
    pq = [(0, start[0], start[1], 0)]
    dist = {}

    while pq:
        score, r, c, d = heapq.heappop(pq)

        state = (r, c, d)
        if state in dist:
            continue
        dist[state] = score

        # Try moving forward
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            new_state = (nr, nc, d)
            if new_state not in dist:
                heapq.heappush(pq, (score + 1, nr, nc, d))

        # Try rotating clockwise
        new_d = (d + 1) % 4
        new_state = (r, c, new_d)
        if new_state not in dist:
            heapq.heappush(pq, (score + 1000, r, c, new_d))

        # Try rotating counterclockwise
        new_d = (d - 1) % 4
        new_state = (r, c, new_d)
        if new_state not in dist:
            heapq.heappush(pq, (score + 1000, r, c, new_d))

    # Find minimum score to reach end
    min_score = float('inf')
    for d in range(4):
        state = (end[0], end[1], d)
        if state in dist:
            min_score = min(min_score, dist[state])

    # Backtrack from end to find all tiles on best paths
    # We'll trace backwards from end states that have the minimum score
    on_best_path = set()
    queue = []
    for d in range(4):
        state = (end[0], end[1], d)
        if state in dist and dist[state] == min_score:
            queue.append(state)
            on_best_path.add(state)

    visited_backtrack = set(queue)

    while queue:
        r, c, d = queue.pop(0)
        current_score = dist[(r, c, d)]

        # Check if we came from moving forward (so go backward now)
        dr, dc = directions[d]
        pr, pc = r - dr, c - dc
        if 0 <= pr < rows and 0 <= pc < cols and grid[pr][pc] != '#':
            prev_state = (pr, pc, d)
            if prev_state in dist and dist[prev_state] == current_score - 1:
                if prev_state not in visited_backtrack:
                    visited_backtrack.add(prev_state)
                    queue.append(prev_state)
                    on_best_path.add(prev_state)

        # Check if we came from rotating clockwise (so rotate counterclockwise now)
        prev_d = (d - 1) % 4
        prev_state = (r, c, prev_d)
        if prev_state in dist and dist[prev_state] == current_score - 1000:
            if prev_state not in visited_backtrack:
                visited_backtrack.add(prev_state)
                queue.append(prev_state)
                on_best_path.add(prev_state)

        # Check if we came from rotating counterclockwise (so rotate clockwise now)
        prev_d = (d + 1) % 4
        prev_state = (r, c, prev_d)
        if prev_state in dist and dist[prev_state] == current_score - 1000:
            if prev_state not in visited_backtrack:
                visited_backtrack.add(prev_state)
                queue.append(prev_state)
                on_best_path.add(prev_state)

    # Extract unique positions (ignoring direction)
    tiles = set()
    for r, c, d in on_best_path:
        tiles.add((r, c))

    return len(tiles)

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
