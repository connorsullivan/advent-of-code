import sys
import os
import re

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_machines(lines):
    """Parse the input to extract claw machine configurations."""
    machines = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("Button A"):
            # Parse Button A
            match_a = re.search(r"X\+(\d+), Y\+(\d+)", lines[i])
            ax, ay = int(match_a.group(1)), int(match_a.group(2))

            # Parse Button B
            match_b = re.search(r"X\+(\d+), Y\+(\d+)", lines[i+1])
            bx, by = int(match_b.group(1)), int(match_b.group(2))

            # Parse Prize
            match_prize = re.search(r"X=(\d+), Y=(\d+)", lines[i+2])
            px, py = int(match_prize.group(1)), int(match_prize.group(2))

            machines.append(((ax, ay), (bx, by), (px, py)))
            i += 4  # Skip to next machine (3 lines + 1 blank)
        else:
            i += 1

    return machines

def solve_machine(button_a, button_b, prize):
    """
    Solve the system of linear equations to find the number of button presses.

    We need to find non-negative integers a and b such that:
    a * ax + b * bx = px
    a * ay + b * by = py

    Using Cramer's rule:
    a = (px * by - py * bx) / (ax * by - ay * bx)
    b = (ax * py - ay * px) / (ax * by - ay * bx)
    """
    ax, ay = button_a
    bx, by = button_b
    px, py = prize

    # Calculate determinant
    det = ax * by - ay * bx

    if det == 0:
        return None  # No unique solution

    # Calculate number of presses using Cramer's rule
    a_numerator = px * by - py * bx
    b_numerator = ax * py - ay * px

    # Check if solutions are integers
    if a_numerator % det != 0 or b_numerator % det != 0:
        return None

    a = a_numerator // det
    b = b_numerator // det

    # Check if solutions are non-negative
    if a < 0 or b < 0:
        return None

    return a, b

def part_one(lines):
    """
    Calculate minimum tokens to win all possible prizes.
    Button A costs 3 tokens, Button B costs 1 token.
    """
    machines = parse_machines(lines)
    total_tokens = 0
    prizes_won = 0

    for button_a, button_b, prize in machines:
        result = solve_machine(button_a, button_b, prize)
        if result:
            a_presses, b_presses = result
            tokens = a_presses * 3 + b_presses * 1
            total_tokens += tokens
            prizes_won += 1

    return total_tokens

def part_two(lines):
    """
    Same as part one, but add 10000000000000 to each prize coordinate.
    """
    machines = parse_machines(lines)
    total_tokens = 0
    prizes_won = 0
    offset = 10000000000000

    for button_a, button_b, (px, py) in machines:
        # Add offset to prize coordinates
        adjusted_prize = (px + offset, py + offset)
        result = solve_machine(button_a, button_b, adjusted_prize)
        if result:
            a_presses, b_presses = result
            tokens = a_presses * 3 + b_presses * 1
            total_tokens += tokens
            prizes_won += 1

    return total_tokens

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
