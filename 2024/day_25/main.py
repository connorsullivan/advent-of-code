import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    # Parse schematics into groups
    schematics = []
    current = []

    for line in lines:
        if line.strip() == "":
            if current:
                schematics.append(current)
                current = []
        else:
            current.append(line.strip())

    if current:
        schematics.append(current)

    locks = []
    keys = []

    # Process each schematic
    for schematic in schematics:
        if len(schematic) == 0:
            continue

        # Check if it's a lock (top row all #) or key (bottom row all #)
        is_lock = schematic[0] == "#####"
        is_key = schematic[-1] == "#####"

        if is_lock:
            # Lock: count # in each column from top (excluding top row)
            heights = []
            for col in range(5):
                height = 0
                for row in range(1, len(schematic)):
                    if schematic[row][col] == '#':
                        height += 1
                    else:
                        break
                heights.append(height)
            locks.append(heights)
        elif is_key:
            # Key: count # in each column from bottom (excluding bottom row)
            heights = []
            for col in range(5):
                height = 0
                for row in range(len(schematic) - 2, -1, -1):
                    if schematic[row][col] == '#':
                        height += 1
                    else:
                        break
                heights.append(height)
            keys.append(heights)

    # Count fitting lock/key pairs
    fit_count = 0
    for lock in locks:
        for key in keys:
            # Check if they fit (sum in each column must be <= 5)
            fits = True
            for col in range(5):
                if lock[col] + key[col] > 5:
                    fits = False
                    break
            if fits:
                fit_count += 1

    return fit_count

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
