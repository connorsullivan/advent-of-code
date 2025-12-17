import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    pos = 50
    count = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        if direction == 'R':
            pos = (pos + distance) % 100
        else:
            pos = (pos - distance) % 100
        if pos == 0:
            count += 1
    return count

def part_two(lines):
    pos = 50
    total_hits = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])

        if direction == 'R':
            # Hits 0 if pos + i is multiple of 100 for 1 <= i <= distance
            # pos + 1 <= 100k <= pos + distance
            hits = (pos + distance) // 100 - pos // 100
            pos = (pos + distance) % 100
        else:
            # Hits 0 if pos - i is multiple of 100 for 1 <= i <= distance
            # pos - distance <= 100k <= pos - 1
            hits = (pos - 1) // 100 - (pos - distance - 1) // 100
            pos = (pos - distance) % 100

        total_hits += hits
    return total_hits

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
