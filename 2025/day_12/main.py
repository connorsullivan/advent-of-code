import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    shapes = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
        if line.endswith(":") and line[:-1].isdigit():
            idx = int(line[:-1])
            area = 0
            i += 1
            for _ in range(3):
                area += lines[i].count("#")
                i += 1
            shapes[idx] = area
        else:
            break
    count_fit = 0
    for j in range(i, len(lines)):
        line = lines[j].strip()
        if not line:
            continue
        dims, rest = line.split(":")
        w, h = map(int, dims.lower().split("x"))
        counts = list(map(int, rest.strip().split()))
        required_area = sum(counts[k] * shapes.get(k, 0) for k in range(len(counts)))
        if required_area <= w * h:
            count_fit += 1
    return count_fit

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
