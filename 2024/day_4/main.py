import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    grid = [line.strip() for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    target = "XMAS"
    target_len = len(target)

    # Directions: (row_change, col_change)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (-1, 1),  # Diagonal Up-Right
        (-1, -1)  # Diagonal Up-Left
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if the word fits in this direction
                if 0 <= r + (target_len - 1) * dr < rows and \
                   0 <= c + (target_len - 1) * dc < cols:
                    match = True
                    for i in range(target_len):
                        if grid[r + i * dr][c + i * dc] != target[i]:
                            match = False
                            break
                    if match:
                        count += 1
    return count

def part_two(lines):
    grid = [line.strip() for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 'A':
                # Check diagonal 1 (top-left to bottom-right)
                tl = grid[r-1][c-1]
                br = grid[r+1][c+1]
                diag1_valid = (tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')

                # Check diagonal 2 (top-right to bottom-left)
                tr = grid[r-1][c+1]
                bl = grid[r+1][c-1]
                diag2_valid = (tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M')

                if diag1_valid and diag2_valid:
                    count += 1
    return count

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
