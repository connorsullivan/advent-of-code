import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    rolls = set()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '@':
                rolls.add((r, c))

    accessible_count = 0
    for r, c in rolls:
        neighbors = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if (r + dr, c + dc) in rolls:
                    neighbors += 1
        if neighbors < 4:
            accessible_count += 1
    return accessible_count

def part_two(lines):
    rolls = set()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '@':
                rolls.add((r, c))

    total_removed = 0
    to_check = set(rolls)

    while True:
        newly_accessible = []
        for r, c in to_check:
            if (r, c) not in rolls:
                continue
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    if (r + dr, c + dc) in rolls:
                        neighbors += 1
            if neighbors < 4:
                newly_accessible.append((r, c))

        if not newly_accessible:
            break

        total_removed += len(newly_accessible)
        next_to_check = set()
        for r, c in newly_accessible:
            rolls.remove((r, c))
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in rolls:
                        next_to_check.add((nr, nc))
        to_check = next_to_check

    return total_removed

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
