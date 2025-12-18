import sys
import os
import re

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _parse(lines: list[str]) -> tuple[list[int], list[tuple[int, int, list[int]]]]:
    shapes: dict[int, list[str]] = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        m = re.match(r"^(\d+):$", line)
        if not m:
            break
        idx = int(m.group(1))
        i += 1
        grid: list[str] = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^\d+x\d+:", lines[i].strip()):
            grid.append(lines[i].strip())
            i += 1
        shapes[idx] = grid
        while i < len(lines) and not lines[i].strip():
            i += 1

    shape_sizes: list[int] = []
    for idx in range(len(shapes)):
        shape_sizes.append(sum(row.count("#") for row in shapes[idx]))

    regions: list[tuple[int, int, list[int]]] = []
    for j in range(i, len(lines)):
        line = lines[j].strip()
        if not line:
            continue
        m = re.match(r"^(\d+)x(\d+):\s*(.*)$", line)
        if not m:
            continue
        w, h = int(m.group(1)), int(m.group(2))
        counts = [int(x) for x in m.group(3).split()]
        regions.append((w, h, counts))
    return shape_sizes, regions


def part_one(lines):
    shape_sizes, regions = _parse(lines)
    ok = 0
    for w, h, counts in regions:
        needed = sum(counts[i] * shape_sizes[i] for i in range(len(counts)))
        if needed <= w * h:
            ok += 1
    return ok

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
