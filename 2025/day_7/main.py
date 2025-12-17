import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    if not lines:
        return 0

    # Find S
    start_col = -1
    for col, char in enumerate(lines[0]):
        if char == 'S':
            start_col = col
            break

    if start_col == -1:
        return 0

    active_beams = {start_col}
    total_splits = 0

    for row in range(1, len(lines)):
        new_active_beams = set()
        for col in active_beams:
            if 0 <= col < len(lines[row]) and lines[row][col] == '^':
                total_splits += 1
                new_active_beams.add(col - 1)
                new_active_beams.add(col + 1)
            else:
                new_active_beams.add(col)
        active_beams = new_active_beams

    return total_splits

def part_two(lines):
    if not lines:
        return 0

    # Find S
    start_col = -1
    for col, char in enumerate(lines[0]):
        if char == 'S':
            start_col = col
            break

    if start_col == -1:
        return 0

    # timelines[col] = number of timelines at this column
    timelines = {start_col: 1}

    for row in range(1, len(lines)):
        new_timelines = {}
        for col, count in timelines.items():
            if 0 <= col < len(lines[row]) and lines[row][col] == '^':
                new_timelines[col - 1] = new_timelines.get(col - 1, 0) + count
                new_timelines[col + 1] = new_timelines.get(col + 1, 0) + count
            else:
                new_timelines[col] = new_timelines.get(col, 0) + count
        timelines = new_timelines

    return sum(timelines.values())

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
