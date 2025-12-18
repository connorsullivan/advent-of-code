import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Count how many times the tachyon beam splits."""
    # Find starting position
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    start_col = -1
    for col in range(cols):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col == -1:
        return 0
    
    # Simulate beam propagation using a set to track unique positions
    beams = {(0, start_col)}
    splits = 0
    
    while beams:
        new_beams = set()
        for row, col in beams:
            # Move down
            next_row = row + 1
            
            # Check if out of bounds
            if next_row >= rows:
                continue
            
            # Check what's at the next position
            if grid[next_row][col] == '^':
                # Split!
                splits += 1
                # Create two new beams: one left, one right
                if col - 1 >= 0:
                    new_beams.add((next_row, col - 1))
                if col + 1 < cols:
                    new_beams.add((next_row, col + 1))
            else:
                # Continue downward
                new_beams.add((next_row, col))
        
        beams = new_beams
    
    return splits

def part_two(lines):
    """Count unique timelines (paths) for quantum tachyon particle."""
    # Find starting position
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    start_col = -1
    for col in range(cols):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col == -1:
        return 0
    
    # Count all possible paths using DFS with memoization
    memo = {}
    
    def count_paths(row, col):
        """Return number of paths from (row, col) to any exit."""
        if (row, col) in memo:
            return memo[(row, col)]
        
        next_row = row + 1
        
        # Out of bounds = reached an exit (1 path completes)
        if next_row >= rows:
            return 1
        
        # Check what's at the next position
        if grid[next_row][col] == '^':
            # Split! Count paths from both branches
            paths = 0
            
            # Go left
            if col - 1 >= 0:
                paths += count_paths(next_row, col - 1)
            
            # Go right
            if col + 1 < cols:
                paths += count_paths(next_row, col + 1)
            
            memo[(row, col)] = paths
            return paths
        else:
            # Continue downward
            paths = count_paths(next_row, col)
            memo[(row, col)] = paths
            return paths
    
    return count_paths(0, start_col)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
