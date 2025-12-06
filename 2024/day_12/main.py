import sys
import os
from collections import deque

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def get_regions(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    regions = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) in visited:
                continue

            plant_type = grid[r][c]
            region_cells = set()
            queue = deque([(r, c)])
            visited.add((r, c))
            region_cells.add((r, c))

            while queue:
                curr_r, curr_c = queue.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = curr_r + dr, curr_c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == plant_type and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            region_cells.add((nr, nc))
                            queue.append((nr, nc))

            regions.append((plant_type, region_cells))
    return regions

def calculate_perimeter(region_cells, grid):
    perimeter = 0
    for r, c in region_cells:
        # Check 4 neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in region_cells:
                perimeter += 1
    return perimeter

def calculate_sides(region_cells, grid):
    top_edges = set()
    bottom_edges = set()
    left_edges = set()
    right_edges = set()

    for r, c in region_cells:
        # Top
        if (r-1, c) not in region_cells:
            top_edges.add((r, c))
        # Bottom
        if (r+1, c) not in region_cells:
            bottom_edges.add((r, c))
        # Left
        if (r, c-1) not in region_cells:
            left_edges.add((r, c))
        # Right
        if (r, c+1) not in region_cells:
            right_edges.add((r, c))

    sides = 0

    # Count top sides
    top_by_row = {}
    for r, c in top_edges:
        if r not in top_by_row:
            top_by_row[r] = []
        top_by_row[r].append(c)

    for r in top_by_row:
        cols_list = sorted(top_by_row[r])
        sides += 1
        for i in range(1, len(cols_list)):
            if cols_list[i] != cols_list[i-1] + 1:
                sides += 1

    # Count bottom sides
    bottom_by_row = {}
    for r, c in bottom_edges:
        if r not in bottom_by_row:
            bottom_by_row[r] = []
        bottom_by_row[r].append(c)

    for r in bottom_by_row:
        cols_list = sorted(bottom_by_row[r])
        sides += 1
        for i in range(1, len(cols_list)):
            if cols_list[i] != cols_list[i-1] + 1:
                sides += 1

    # Count left sides
    left_by_col = {}
    for r, c in left_edges:
        if c not in left_by_col:
            left_by_col[c] = []
        left_by_col[c].append(r)

    for c in left_by_col:
        rows_list = sorted(left_by_col[c])
        sides += 1
        for i in range(1, len(rows_list)):
            if rows_list[i] != rows_list[i-1] + 1:
                sides += 1

    # Count right sides
    right_by_col = {}
    for r, c in right_edges:
        if c not in right_by_col:
            right_by_col[c] = []
        right_by_col[c].append(r)

    for c in right_by_col:
        rows_list = sorted(right_by_col[c])
        sides += 1
        for i in range(1, len(rows_list)):
            if rows_list[i] != rows_list[i-1] + 1:
                sides += 1

    return sides

def part_one(lines):
    grid = [line.strip() for line in lines]
    regions = get_regions(grid)

    total_price = 0
    for plant_type, cells in regions:
        area = len(cells)
        perimeter = calculate_perimeter(cells, grid)
        total_price += area * perimeter

    return total_price

def part_two(lines):
    grid = [line.strip() for line in lines]
    regions = get_regions(grid)

    total_price = 0
    for plant_type, cells in regions:
        area = len(cells)
        sides = calculate_sides(cells, grid)
        total_price += area * sides

    return total_price

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
