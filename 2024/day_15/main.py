import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    """Parse the input into a grid and moves."""
    grid = []
    moves = []
    parsing_grid = True

    for line in lines:
        line = line.strip()
        if not line:
            parsing_grid = False
            continue

        if parsing_grid:
            grid.append(list(line))
        else:
            moves.extend(list(line))

    return grid, moves

def find_robot(grid):
    """Find the robot's position in the grid."""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                return r, c
    return None

def move_robot(grid, r, c, dr, dc):
    """
    Try to move the robot and push boxes if needed.
    Returns (new_r, new_c) if the move was successful, otherwise (r, c).
    """
    nr, nc = r + dr, c + dc

    # Check if next position is a wall
    if grid[nr][nc] == '#':
        return r, c

    # If next position is empty, just move
    if grid[nr][nc] == '.':
        grid[r][c] = '.'
        grid[nr][nc] = '@'
        return nr, nc

    # If next position is a box, try to push it
    if grid[nr][nc] == 'O':
        # Find all boxes in a line
        boxes_to_push = []
        check_r, check_c = nr, nc

        while grid[check_r][check_c] == 'O':
            boxes_to_push.append((check_r, check_c))
            check_r += dr
            check_c += dc

        # Check if we can push all boxes (next position must be empty)
        if grid[check_r][check_c] == '.':
            # Push boxes from the end
            grid[check_r][check_c] = 'O'
            grid[nr][nc] = '@'
            grid[r][c] = '.'
            return nr, nc

    return r, c

def calculate_gps(grid):
    """Calculate the sum of GPS coordinates for all boxes."""
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                total += 100 * r + c
    return total

def part_one(lines):
    grid, moves = parse_input(lines)
    r, c = find_robot(grid)

    # Direction mappings
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    # Execute all moves
    for move in moves:
        dr, dc = directions[move]
        r, c = move_robot(grid, r, c, dr, dc)

    return calculate_gps(grid)

def scale_grid(grid):
    """Scale the grid for part 2."""
    scaled = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == '#':
                new_row.extend(['#', '#'])
            elif cell == 'O':
                new_row.extend(['[', ']'])
            elif cell == '.':
                new_row.extend(['.', '.'])
            elif cell == '@':
                new_row.extend(['@', '.'])
        scaled.append(new_row)
    return scaled

def can_push_wide_box(grid, r, c, dr, dc, visited=None):
    """
    Check if we can push a wide box (and any boxes it would push).
    This is recursive and handles vertical pushes that affect multiple boxes.
    """
    if visited is None:
        visited = set()

    # If we've already checked this position, return True
    if (r, c) in visited:
        return True
    visited.add((r, c))

    cell = grid[r][c]

    # If empty, we can push here
    if cell == '.':
        return True

    # If wall, we can't push
    if cell == '#':
        return False

    # For wide boxes
    if cell == '[':
        left_r, left_c = r, c
        right_r, right_c = r, c + 1
    elif cell == ']':
        left_r, left_c = r, c - 1
        right_r, right_c = r, c
    else:
        return True  # Not a box

    # Mark both halves as visited
    visited.add((left_r, left_c))
    visited.add((right_r, right_c))

    # For horizontal movement, check the next position in the direction
    if dr == 0:
        if dc == -1:  # Moving left
            next_r, next_c = left_r + dr, left_c + dc
        else:  # Moving right
            next_r, next_c = right_r + dr, right_c + dc
        return can_push_wide_box(grid, next_r, next_c, dr, dc, visited)

    # For vertical movement, check both positions above/below the box
    else:
        left_next_r, left_next_c = left_r + dr, left_c + dc
        right_next_r, right_next_c = right_r + dr, right_c + dc
        return (can_push_wide_box(grid, left_next_r, left_next_c, dr, dc, visited) and
                can_push_wide_box(grid, right_next_r, right_next_c, dr, dc, visited))

def push_wide_boxes(grid, r, c, dr, dc, moved=None):
    """
    Actually push the wide boxes. Must be called after can_push_wide_box returns True.
    """
    if moved is None:
        moved = set()

    if (r, c) in moved:
        return

    cell = grid[r][c]

    # If empty or wall, nothing to do
    if cell == '.' or cell == '#':
        return

    # Find the box parts
    if cell == '[':
        left_r, left_c = r, c
        right_r, right_c = r, c + 1
    elif cell == ']':
        left_r, left_c = r, c - 1
        right_r, right_c = r, c
    else:
        return  # Not a box

    # Mark as moved
    moved.add((left_r, left_c))
    moved.add((right_r, right_c))

    # For horizontal movement
    if dr == 0:
        if dc == -1:  # Moving left
            # First push anything to the left
            push_wide_boxes(grid, left_r + dr, left_c + dc, dr, dc, moved)
            # Then move this box
            grid[left_r][left_c + dc] = '['
            grid[right_r][right_c + dc] = ']'
            grid[right_r][right_c] = '.'
        else:  # Moving right
            # First push anything to the right
            push_wide_boxes(grid, right_r + dr, right_c + dc, dr, dc, moved)
            # Then move this box
            grid[left_r][left_c + dc] = '['
            grid[right_r][right_c + dc] = ']'
            grid[left_r][left_c] = '.'
    # For vertical movement
    else:
        # First push anything above/below both halves
        push_wide_boxes(grid, left_r + dr, left_c + dc, dr, dc, moved)
        push_wide_boxes(grid, right_r + dr, right_c + dc, dr, dc, moved)
        # Then move this box
        grid[left_r + dr][left_c + dc] = '['
        grid[right_r + dr][right_c + dc] = ']'
        grid[left_r][left_c] = '.'
        grid[right_r][right_c] = '.'

def move_robot_wide(grid, r, c, dr, dc):
    """
    Try to move the robot in the scaled grid with wide boxes.
    """
    nr, nc = r + dr, c + dc

    # Check if next position is a wall
    if grid[nr][nc] == '#':
        return r, c

    # If next position is empty, just move
    if grid[nr][nc] == '.':
        grid[r][c] = '.'
        grid[nr][nc] = '@'
        return nr, nc

    # If next position is a wide box part
    if grid[nr][nc] in ['[', ']']:
        # Check if we can push
        if can_push_wide_box(grid, nr, nc, dr, dc):
            # Push the boxes
            push_wide_boxes(grid, nr, nc, dr, dc)
            # Move the robot
            grid[r][c] = '.'
            grid[nr][nc] = '@'
            return nr, nc

    return r, c

def calculate_gps_wide(grid):
    """Calculate the sum of GPS coordinates for all wide boxes."""
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '[':
                total += 100 * r + c
    return total

def part_two(lines):
    grid, moves = parse_input(lines)
    grid = scale_grid(grid)
    r, c = find_robot(grid)

    # Direction mappings
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    # Execute all moves
    for move in moves:
        dr, dc = directions[move]
        r, c = move_robot_wide(grid, r, c, dr, dc)

    return calculate_gps_wide(grid)

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
