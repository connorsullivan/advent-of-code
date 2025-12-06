import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_schematics(lines):
    locks = []
    keys = []

    current_schematic = []
    for line in lines:
        if not line:
            if current_schematic:
                process_schematic(current_schematic, locks, keys)
                current_schematic = []
        else:
            current_schematic.append(line)

    if current_schematic:
        process_schematic(current_schematic, locks, keys)

    return locks, keys

def process_schematic(schematic, locks, keys):
    # Determine if lock or key
    # Locks have the top row filled (#####)
    # Keys have the top row empty (.....) - wait, checking the example
    # Lock:
    # #####
    # .####
    # ...
    # Key:
    # .....
    # #....
    # ...

    is_lock = schematic[0] == "#####"

    heights = []
    width = len(schematic[0])
    for col in range(width):
        count = 0
        for row in range(len(schematic)):
            if schematic[row][col] == '#':
                count += 1
        heights.append(count - 1)

    if is_lock:
        locks.append(tuple(heights))
    else:
        keys.append(tuple(heights))

def part_one(lines):
    locks, keys = parse_schematics(lines)

    fit_count = 0
    for lock in locks:
        for key in keys:
            fits = True
            for l, k in zip(lock, key):
                if l + k > 5:
                    fits = False
                    break
            if fits:
                fit_count += 1

    return fit_count

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
