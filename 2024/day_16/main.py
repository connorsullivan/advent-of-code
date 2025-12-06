import sys
import os
import heapq

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def dijkstra(grid, start_nodes, is_backward=False):
    rows = len(grid)
    cols = len(grid[0])
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    dist = {}
    pq = []

    for node in start_nodes:
        # node is (cost, r, c, d)
        dist[(node[1], node[2], node[3])] = node[0]
        heapq.heappush(pq, node)

    while pq:
        cost, r, c, d = heapq.heappop(pq)

        if cost > dist.get((r, c, d), float('inf')):
            continue

        # Transitions
        moves = []

        if not is_backward:
            # Forward moves
            # 1. Move forward
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                moves.append((1, nr, nc, d))
            # 2. Rotate clockwise
            moves.append((1000, r, c, (d + 1) % 4))
            # 3. Rotate counter-clockwise
            moves.append((1000, r, c, (d - 1) % 4))
        else:
            # Backward moves
            # 1. Move backward (reverse of moving forward)
            # To have arrived at (r, c) facing d from (pr, pc), we must have moved forward from (pr, pc) facing d.
            # So (pr, pc) = (r - dr[d], c - dc[d])
            pr, pc = r - dr[d], c - dc[d]
            if 0 <= pr < rows and 0 <= pc < cols and grid[pr][pc] != '#':
                moves.append((1, pr, pc, d))
            # 2. Rotate (reverse of rotating)
            # If we arrived at d by rotating clockwise from d-1, then previous was d-1.
            moves.append((1000, r, c, (d - 1) % 4))
            # If we arrived at d by rotating ccw from d+1, then previous was d+1.
            moves.append((1000, r, c, (d + 1) % 4))

        for weight, nr, nc, nd in moves:
            new_cost = cost + weight
            if new_cost < dist.get((nr, nc, nd), float('inf')):
                dist[(nr, nc, nd)] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc, nd))

    return dist

def solve(lines):
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    start_pos = None
    end_pos = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)
            elif grid[r][c] == 'E':
                end_pos = (r, c)

    # Part 1
    # Start facing East (0)
    dist_from_start = dijkstra(grid, [(0, start_pos[0], start_pos[1], 0)], is_backward=False)

    min_cost = float('inf')
    for d in range(4):
        if (end_pos[0], end_pos[1], d) in dist_from_start:
            min_cost = min(min_cost, dist_from_start[(end_pos[0], end_pos[1], d)])

    # Part 2
    dist_to_end = dijkstra(grid, [(0, end_pos[0], end_pos[1], d) for d in range(4)], is_backward=True)

    optimal_tiles = set()
    for r in range(rows):
        for c in range(cols):
            for d in range(4):
                state = (r, c, d)
                if state in dist_from_start and state in dist_to_end:
                    if dist_from_start[state] + dist_to_end[state] == min_cost:
                        optimal_tiles.add((r, c))

    return min_cost, len(optimal_tiles)

def part_one(lines):
    cost, _ = solve(lines)
    return cost

def part_two(lines):
    _, tiles = solve(lines)
    return tiles

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
