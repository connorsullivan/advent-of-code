import sys
import os
from collections import defaultdict
from itertools import combinations

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """
    Find antinodes where one antenna is exactly twice as far as the other.
    For each pair of antennas with same frequency, create two antinodes:
    - One on the far side of the first antenna
    - One on the far side of the second antenna
    """
    # Parse the grid to find all antennas
    antennas = defaultdict(list)
    height = len(lines)
    width = len(lines[0]) if height > 0 else 0

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char != '.':
                antennas[char].append((r, c))

    # Find all antinodes
    antinodes = set()

    for freq, positions in antennas.items():
        # Check all pairs of antennas with the same frequency
        for (r1, c1), (r2, c2) in combinations(positions, 2):
            # Calculate the vector from antenna 1 to antenna 2
            dr = r2 - r1
            dc = c2 - c1

            # Antinode on the far side of antenna 2 (antenna 1 is closer)
            antinode1 = (r2 + dr, c2 + dc)
            if 0 <= antinode1[0] < height and 0 <= antinode1[1] < width:
                antinodes.add(antinode1)

            # Antinode on the far side of antenna 1 (antenna 2 is closer)
            antinode2 = (r1 - dr, c1 - dc)
            if 0 <= antinode2[0] < height and 0 <= antinode2[1] < width:
                antinodes.add(antinode2)

    return len(antinodes)

def part_two(lines):
    """
    Find antinodes at any position in line with at least two antennas of same frequency.
    This includes the antenna positions themselves.
    """
    # Parse the grid to find all antennas
    antennas = defaultdict(list)
    height = len(lines)
    width = len(lines[0]) if height > 0 else 0

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char != '.':
                antennas[char].append((r, c))

    # Find all antinodes
    antinodes = set()

    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue

        # Check all pairs of antennas with the same frequency
        for (r1, c1), (r2, c2) in combinations(positions, 2):
            # Calculate the vector from antenna 1 to antenna 2
            dr = r2 - r1
            dc = c2 - c1

            # Reduce to simplest form (GCD)
            from math import gcd
            g = gcd(abs(dr), abs(dc))
            dr //= g
            dc //= g

            # Add all points in line with the two antennas
            # Start from antenna 1 and go backwards
            r, c = r1, c1
            while 0 <= r < height and 0 <= c < width:
                antinodes.add((r, c))
                r -= dr
                c -= dc

            # Start from antenna 1 and go forwards
            r, c = r1 + dr, c1 + dc
            while 0 <= r < height and 0 <= c < width:
                antinodes.add((r, c))
                r += dr
                c += dc

    return len(antinodes)

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
