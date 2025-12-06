import sys
import os
import math

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_grid(lines):
    antennas = {}
    rows = len(lines)
    cols = len(lines[0])
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))
    return antennas, rows, cols

def part_one(lines):
    antennas, rows, cols = parse_grid(lines)
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                # Vector from 1 to 2
                dr = r2 - r1
                dc = c2 - c1

                # Antinode 1: Before 1 (r1 - dr, c1 - dc)
                ar1, ac1 = r1 - dr, c1 - dc
                # Antinode 2: After 2 (r2 + dr, c2 + dc)
                ar2, ac2 = r2 + dr, c2 + dc

                if 0 <= ar1 < rows and 0 <= ac1 < cols:
                    antinodes.add((ar1, ac1))

                if 0 <= ar2 < rows and 0 <= ac2 < cols:
                    antinodes.add((ar2, ac2))

    return len(antinodes)

def part_two(lines):
    antennas, rows, cols = parse_grid(lines)
    antinodes = set()

    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue

        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                dr = r2 - r1
                dc = c2 - c1

                # Simplify the vector to find all grid points on the line
                g = math.gcd(dr, dc)
                dr //= g
                dc //= g

                # Go in positive direction from r1, c1
                curr_r, curr_c = r1, c1
                while 0 <= curr_r < rows and 0 <= curr_c < cols:
                    antinodes.add((curr_r, curr_c))
                    curr_r += dr
                    curr_c += dc

                # Go in negative direction from r1, c1
                curr_r, curr_c = r1, c1
                while 0 <= curr_r < rows and 0 <= curr_c < cols:
                    antinodes.add((curr_r, curr_c))
                    curr_r -= dr
                    curr_c -= dc

    return len(antinodes)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
