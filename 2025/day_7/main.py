import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Count total splitters hit by beams."""
    if not lines:
        return 0
    
    grid = [list(line) for line in lines if line]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find the starting position (S)
    start_col = None
    for c in range(cols):
        if grid[0][c] == 'S':
            start_col = c
            break
    
    if start_col is None:
        return 0
    
    splits = 0
    # Track which columns have active beams (any beam reaching that column)
    beams = {start_col}  # Set of columns
    
    for row in range(1, rows):
        new_beams = set()
        for col in beams:
            if grid[row][col] == '^':
                # Splitter - count this once
                splits += 1
                left_col = col - 1
                right_col = col + 1
                if left_col >= 0:
                    new_beams.add(left_col)
                if right_col < cols:
                    new_beams.add(right_col)
            else:
                # Continue straight down
                new_beams.add(col)
        beams = new_beams
        if not beams:
            break
    
    return splits

def part_two(lines):
    """Count total timelines (paths through the manifold)."""
    if not lines:
        return 0
    
    grid = [list(line) for line in lines if line]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find the starting position (S)
    start_col = None
    for c in range(cols):
        if grid[0][c] == 'S':
            start_col = c
            break
    
    if start_col is None:
        return 0
    
    # Count the number of distinct paths (timelines)
    # Each split doubles the path count
    # Track beam positions and how many paths lead to each
    beams = {start_col: 1}  # column -> number of paths to this position
    
    for row in range(1, rows):
        new_beams = {}
        for col, paths in beams.items():
            if grid[row][col] == '^':
                # Splitter - each path splits into two timelines
                left_col = col - 1
                right_col = col + 1
                if left_col >= 0:
                    new_beams[left_col] = new_beams.get(left_col, 0) + paths
                if right_col < cols:
                    new_beams[right_col] = new_beams.get(right_col, 0) + paths
            else:
                # Continue straight down
                new_beams[col] = new_beams.get(col, 0) + paths
        beams = new_beams
        if not beams:
            break
    
    # Total timelines is the sum of all paths at the end
    return sum(beams.values())

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
