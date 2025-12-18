import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def count_neighbors(grid, row, col):
    """Count the number of '@' neighbors (including diagonals) for a position."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0
    
    # Check all 8 adjacent positions
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                count += 1
    
    return count

def part_one(lines):
    """Count rolls of paper accessible by forklifts (< 4 neighbors)."""
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    accessible = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                neighbors = count_neighbors(grid, row, col)
                if neighbors < 4:
                    accessible += 1
    
    return accessible

def part_two(lines):
    """Count total rolls that can be removed by repeatedly removing accessible ones."""
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    total_removed = 0
    
    while True:
        # Find all accessible rolls in current state
        accessible = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '@':
                    neighbors = count_neighbors(grid, row, col)
                    if neighbors < 4:
                        accessible.append((row, col))
        
        if not accessible:
            break
        
        # Remove all accessible rolls
        for row, col in accessible:
            grid[row][col] = '.'
        
        total_removed += len(accessible)
    
    return total_removed

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
