import sys
import os
import re

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_line(line):
    match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
    if match:
        return list(map(int, match.groups()))
    return None

def part_one(lines):
    width = 101
    height = 103
    time = 100

    robots = [parse_line(line) for line in lines]
    robots = [r for r in robots if r is not None]

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    mid_x = width // 2
    mid_y = height // 2

    for px, py, vx, vy in robots:
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height

        if final_x < mid_x and final_y < mid_y:
            q1 += 1
        elif final_x > mid_x and final_y < mid_y:
            q2 += 1
        elif final_x < mid_x and final_y > mid_y:
            q3 += 1
        elif final_x > mid_x and final_y > mid_y:
            q4 += 1

    return q1 * q2 * q3 * q4

def part_two(lines):
    width = 101
    height = 103
    robots = [parse_line(line) for line in lines]
    robots = [r for r in robots if r is not None]

    max_neighbors = -1
    best_time = -1

    # The pattern repeats every width * height seconds because 101 and 103 are prime.
    # Actually 101 and 103 are coprime, so LCM is product.
    period = width * height

    for t in range(1, period + 1):
        positions = set()
        for px, py, vx, vy in robots:
            final_x = (px + vx * t) % width
            final_y = (py + vy * t) % height
            positions.add((final_x, final_y))

        # Count neighbors
        neighbor_count = 0
        for x, y in positions:
            # Check 4 neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (x + dx, y + dy) in positions:
                    neighbor_count += 1

        if neighbor_count > max_neighbors:
            max_neighbors = neighbor_count
            best_time = t

    # Visualize the best time
    with open("tree_visualization.txt", "w") as f:
        f.write(f"Time: {best_time}\n")
        positions = set()
        for px, py, vx, vy in robots:
            final_x = (px + vx * best_time) % width
            final_y = (py + vy * best_time) % height
            positions.add((final_x, final_y))

        for y in range(height):
            row = ""
            for x in range(width):
                if (x, y) in positions:
                    row += "#"
                else:
                    row += "."
            f.write(row + "\n")

    return best_time

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
