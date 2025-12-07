import sys
import os
from collections import deque

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def find_regions(grid):
    """Find all regions using flood fill (BFS)."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = []

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                # Start a new region
                plant_type = grid[r][c]
                region = []
                queue = deque([(r, c)])
                visited[r][c] = True

                while queue:
                    curr_r, curr_c = queue.popleft()
                    region.append((curr_r, curr_c))

                    # Check all 4 neighbors
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == plant_type:
                            visited[nr][nc] = True
                            queue.append((nr, nc))

                regions.append((plant_type, region))

    return regions

def calculate_perimeter(region, grid):
    """Calculate perimeter by counting sides that don't touch same region."""
    rows, cols = len(grid), len(grid[0])
    region_set = set(region)
    perimeter = 0

    for r, c in region:
        # Check all 4 sides
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            # If neighbor is outside grid or not in same region, it's a perimeter side
            if not (0 <= nr < rows and 0 <= nc < cols and (nr, nc) in region_set):
                perimeter += 1

    return perimeter

def count_sides(region, grid):
    """Count the number of distinct sides (continuous edges) of a region."""
    # A side is a continuous straight section of fence
    # We need to count horizontal and vertical sides separately

    region_set = set(region)
    rows, cols = len(grid), len(grid[0])

    # Count horizontal sides (top and bottom edges)
    horizontal_sides = 0

    # Top edges: for each row, find continuous segments where there's an edge on top
    for r in range(rows):
        in_top_edge = False
        for c in range(cols):
            if (r, c) in region_set:
                # Check if there's a top edge (no neighbor above or neighbor is different region)
                has_top_edge = r == 0 or (r - 1, c) not in region_set
                if has_top_edge:
                    if not in_top_edge:
                        horizontal_sides += 1
                        in_top_edge = True
                else:
                    in_top_edge = False
            else:
                in_top_edge = False

    # Bottom edges
    for r in range(rows):
        in_bottom_edge = False
        for c in range(cols):
            if (r, c) in region_set:
                # Check if there's a bottom edge
                has_bottom_edge = r == rows - 1 or (r + 1, c) not in region_set
                if has_bottom_edge:
                    if not in_bottom_edge:
                        horizontal_sides += 1
                        in_bottom_edge = True
                else:
                    in_bottom_edge = False
            else:
                in_bottom_edge = False

    # Count vertical sides (left and right edges)
    vertical_sides = 0

    # Left edges: for each column, find continuous segments where there's an edge on left
    for c in range(cols):
        in_left_edge = False
        for r in range(rows):
            if (r, c) in region_set:
                # Check if there's a left edge
                has_left_edge = c == 0 or (r, c - 1) not in region_set
                if has_left_edge:
                    if not in_left_edge:
                        vertical_sides += 1
                        in_left_edge = True
                else:
                    in_left_edge = False
            else:
                in_left_edge = False

    # Right edges
    for c in range(cols):
        in_right_edge = False
        for r in range(rows):
            if (r, c) in region_set:
                # Check if there's a right edge
                has_right_edge = c == cols - 1 or (r, c + 1) not in region_set
                if has_right_edge:
                    if not in_right_edge:
                        vertical_sides += 1
                        in_right_edge = True
                else:
                    in_right_edge = False
            else:
                in_right_edge = False

    return horizontal_sides + vertical_sides

def part_one(lines):
    grid = [list(line.strip()) for line in lines if line.strip()]
    regions = find_regions(grid)

    total_price = 0
    for plant_type, region in regions:
        area = len(region)
        perimeter = calculate_perimeter(region, grid)
        price = area * perimeter
        total_price += price

    return total_price

def part_two(lines):
    grid = [list(line.strip()) for line in lines if line.strip()]
    regions = find_regions(grid)

    total_price = 0
    for plant_type, region in regions:
        area = len(region)
        sides = count_sides(region, grid)
        price = area * sides
        total_price += price

    return total_price

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
