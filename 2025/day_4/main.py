import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def count_neighbors(grid, row, col):
    """Count the number of paper rolls in adjacent positions."""
    count = 0
    rows, cols = len(grid), len(grid[0])
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                count += 1
    return count

def part_one(lines):
    """Count paper rolls that can be accessed by forklift (< 4 neighbors)."""
    grid = [list(line) for line in lines if line]
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_neighbors(grid, r, c) < 4:
                    count += 1
    
    return count

def part_two(lines):
    """Count total paper rolls that can be removed by repeatedly removing accessible rolls."""
    grid = [list(line) for line in lines if line]
    total_removed = 0
    rows, cols = len(grid), len(grid[0])
    
    while True:
        # Find all currently accessible rolls
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    if count_neighbors(grid, r, c) < 4:
                        to_remove.append((r, c))
        
        if not to_remove:
            break
        
        # Remove them all
        for r, c in to_remove:
            grid[r][c] = '.'
        total_removed += len(to_remove)
    
    return total_removed

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
