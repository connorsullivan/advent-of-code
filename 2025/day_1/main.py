import sys
import os
from typing import Iterable

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _parse_rotations(lines: Iterable[str]) -> list[tuple[int, int]]:
    rotations: list[tuple[int, int]] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            rotations.append((-1, distance))
        elif direction == "R":
            rotations.append((1, distance))
        else:
            raise ValueError(f"Invalid rotation: {line!r}")
    return rotations


def part_one(lines):
    rotations = _parse_rotations(lines)
    pos = 50
    hits = 0
    for sign, distance in rotations:
        pos = (pos + sign * distance) % 100
        if pos == 0:
            hits += 1
    return hits

def part_two(lines):
    rotations = _parse_rotations(lines)
    pos = 50
    hits = 0
    for sign, distance in rotations:
        # Count k in [1..distance] such that (pos + sign*k) % 100 == 0.
        if sign == 1:
            k0 = (-pos) % 100
        else:
            k0 = pos % 100
        if k0 == 0:
            k0 = 100
        if k0 <= distance:
            hits += 1 + (distance - k0) // 100
        pos = (pos + sign * distance) % 100
    return hits

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
