import sys
import os
import re

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    machines = []
    current_machine = {}
    for line in lines:
        line = line.strip()
        if not line:
            if current_machine:
                machines.append(current_machine)
                current_machine = {}
            continue

        if line.startswith("Button A"):
            match = re.search(r"X\+(\d+), Y\+(\d+)", line)
            if match:
                current_machine['A'] = (int(match.group(1)), int(match.group(2)))
        elif line.startswith("Button B"):
            match = re.search(r"X\+(\d+), Y\+(\d+)", line)
            if match:
                current_machine['B'] = (int(match.group(1)), int(match.group(2)))
        elif line.startswith("Prize"):
            match = re.search(r"X=(\d+), Y=(\d+)", line)
            if match:
                current_machine['P'] = (int(match.group(1)), int(match.group(2)))

    if current_machine:
        machines.append(current_machine)
    return machines

def solve_machine(machine, limit=None):
    ax, ay = machine['A']
    bx, by = machine['B']
    px, py = machine['P']

    # Cramer's rule
    # ax * A + bx * B = px
    # ay * A + by * B = py

    det = ax * by - ay * bx
    if det == 0:
        # Parallel lines.
        # Check if they are collinear and if there's a solution.
        # For AoC Day 13, usually we can ignore this or handle if it comes up.
        # If they are collinear, we want to minimize 3*A + B.
        # Since 3*A + B is the cost, and we want to reach (px, py).
        # If collinear, (bx, by) = k * (ax, ay).
        # If k > 3, we prefer A (cost 3 vs cost k). If k < 3, we prefer B.
        # But let's wait to see if this case exists.
        return 0

    a_num = px * by - py * bx
    b_num = ax * py - ay * px

    if a_num % det != 0 or b_num % det != 0:
        return 0

    a = a_num // det
    b = b_num // det

    if a < 0 or b < 0:
        return 0

    if limit is not None:
        if a > limit or b > limit:
            return 0

    return 3 * a + b

def part_one(lines):
    machines = parse_input(lines)
    total_tokens = 0
    for machine in machines:
        cost = solve_machine(machine, limit=100)
        total_tokens += cost
    return total_tokens

def part_two(lines):
    machines = parse_input(lines)
    total_tokens = 0
    offset = 10000000000000
    for machine in machines:
        machine['P'] = (machine['P'][0] + offset, machine['P'][1] + offset)
        cost = solve_machine(machine, limit=None)
        total_tokens += cost
    return total_tokens

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
