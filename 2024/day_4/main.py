import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Find all occurrences of XMAS in the grid (all 8 directions)."""
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # All 8 directions: right, left, down, up, and 4 diagonals
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]

    target = "XMAS"

    def search_from(r, c, dr, dc):
        """Search for XMAS starting from (r, c) in direction (dr, dc)."""
        for i in range(len(target)):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                return False
            if grid[nr][nc] != target[i]:
                return False
        return True

    # Try starting from every position
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if search_from(r, c, dr, dc):
                    count += 1

    return count

def part_two(lines):
    """Find all X-MAS patterns (two MAS forming an X)."""
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # For an X-MAS pattern, we check if 'A' is at the center
    # and MAS forms on both diagonals
    def check_xmas(r, c):
        """Check if (r, c) is the center of an X-MAS pattern."""
        if grid[r][c] != 'A':
            return False

        # Check bounds for all 4 corners
        if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
            return False

        # Get the 4 corners
        top_left = grid[r-1][c-1]
        top_right = grid[r-1][c+1]
        bottom_left = grid[r+1][c-1]
        bottom_right = grid[r+1][c+1]

        # Check diagonal 1 (top-left to bottom-right)
        diag1 = top_left + 'A' + bottom_right
        # Check diagonal 2 (top-right to bottom-left)
        diag2 = top_right + 'A' + bottom_left

        # Both diagonals must be either "MAS" or "SAM"
        valid = diag1 in ["MAS", "SAM"] and diag2 in ["MAS", "SAM"]
        return valid

    # Check every possible center position
    for r in range(rows):
        for c in range(cols):
            if check_xmas(r, c):
                count += 1

    return count

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
