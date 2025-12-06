import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    grid = []
    moves = ""
    parsing_grid = True
    for line in lines:
        if line == "":
            parsing_grid = False
            continue
        if parsing_grid:
            grid.append(list(line))
        else:
            moves += line
    return grid, moves

def find_robot(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == '@':
                return r, c
    return None

def solve_part_one(grid, moves):
    rows = len(grid)
    cols = len(grid[0])
    r, c = find_robot(grid)

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    for move in moves:
        dr, dc = directions[move]
        nr, nc = r + dr, c + dc

        if grid[nr][nc] == '#':
            continue
        elif grid[nr][nc] == '.':
            grid[r][c] = '.'
            grid[nr][nc] = '@'
            r, c = nr, nc
        elif grid[nr][nc] == 'O':
            # Check if we can push
            cr, cc = nr, nc
            while grid[cr][cc] == 'O':
                cr += dr
                cc += dc

            if grid[cr][cc] == '#':
                continue
            elif grid[cr][cc] == '.':
                # Push boxes
                grid[cr][cc] = 'O'
                grid[nr][nc] = '@'
                grid[r][c] = '.'
                r, c = nr, nc

    total_gps = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'O':
                total_gps += 100 * r + c

    return total_gps

def part_one(lines):
    grid, moves = parse_input(lines)
    return solve_part_one(grid, moves)

def expand_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for char in row:
            if char == '#':
                new_row.extend(['#', '#'])
            elif char == 'O':
                new_row.extend(['[', ']'])
            elif char == '.':
                new_row.extend(['.', '.'])
            elif char == '@':
                new_row.extend(['@', '.'])
        new_grid.append(new_row)
    return new_grid

def solve_part_two(grid, moves):
    rows = len(grid)
    cols = len(grid[0])
    r, c = find_robot(grid)

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    for move in moves:
        dr, dc = directions[move]
        nr, nc = r + dr, c + dc

        if grid[nr][nc] == '#':
            continue
        elif grid[nr][nc] == '.':
            grid[r][c] = '.'
            grid[nr][nc] = '@'
            r, c = nr, nc
        elif grid[nr][nc] in ['[', ']']:
            if dr == 0: # Horizontal
                cr, cc = nr, nc
                while grid[cr][cc] in ['[', ']']:
                    cc += dc

                if grid[cr][cc] == '#':
                    continue
                elif grid[cr][cc] == '.':
                    # Shift boxes
                    # Iterate from the empty space back to the robot's target
                    # If moving right (>), dc=1. cc is the empty space. nc is the first box part.
                    # We want to move grid[r][nc...cc-1] to grid[r][nc+1...cc]

                    while cc != nc:
                        grid[cr][cc] = grid[cr][cc-dc]
                        cc -= dc

                    grid[nr][nc] = '@'
                    grid[r][c] = '.'
                    r, c = nr, nc
            else: # Vertical
                # Find all boxes that need to move
                boxes_to_move = set()
                q = []

                # Initial box check
                if grid[nr][nc] == '[':
                    boxes_to_move.add((nr, nc))
                    q.append((nr, nc))
                elif grid[nr][nc] == ']':
                    boxes_to_move.add((nr, nc-1))
                    q.append((nr, nc-1))

                blocked = False
                while q:
                    br, bc = q.pop(0) # Box left coordinate

                    # Check the two positions this box would move into
                    next_r = br + dr
                    check_cols = [bc, bc + 1]

                    for check_c in check_cols:
                        if grid[next_r][check_c] == '#':
                            blocked = True
                            break
                        elif grid[next_r][check_c] == '[':
                            if (next_r, check_c) not in boxes_to_move:
                                boxes_to_move.add((next_r, check_c))
                                q.append((next_r, check_c))
                        elif grid[next_r][check_c] == ']':
                            if (next_r, check_c-1) not in boxes_to_move:
                                boxes_to_move.add((next_r, check_c-1))
                                q.append((next_r, check_c-1))
                    if blocked:
                        break

                if not blocked:
                    # Move all boxes
                    # First clear them
                    for br, bc in boxes_to_move:
                        grid[br][bc] = '.'
                        grid[br][bc+1] = '.'

                    # Then place them in new positions
                    for br, bc in boxes_to_move:
                        grid[br+dr][bc] = '['
                        grid[br+dr][bc+1] = ']'

                    # Move robot
                    grid[r][c] = '.'
                    grid[nr][nc] = '@'
                    r, c = nr, nc

    total_gps = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '[':
                total_gps += 100 * r + c

    return total_gps

def part_two(lines):
    grid, moves = parse_input(lines)
    expanded_grid = expand_grid(grid)
    return solve_part_two(expanded_grid, moves)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
