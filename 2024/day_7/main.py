import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from itertools import product

def parse_equation(line):
    """Parse a line into test value and list of numbers."""
    parts = line.strip().split(':')
    test_value = int(parts[0])
    numbers = list(map(int, parts[1].strip().split()))
    return test_value, numbers

def evaluate_left_to_right(numbers, operators):
    """Evaluate numbers with operators from left to right."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result = result + numbers[i + 1]
        elif op == '*':
            result = result * numbers[i + 1]
        elif op == '||':
            # Concatenation operator
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_produce_value(test_value, numbers, available_ops):
    """Check if we can produce test_value using any combination of operators."""
    if len(numbers) == 1:
        return numbers[0] == test_value

    # Try all combinations of operators
    num_operators = len(numbers) - 1
    for ops in product(available_ops, repeat=num_operators):
        if evaluate_left_to_right(numbers, ops) == test_value:
            return True
    return False

def part_one(lines):
    total = 0
    for line in lines:
        if not line.strip():
            continue
        test_value, numbers = parse_equation(line)
        if can_produce_value(test_value, numbers, ['+', '*']):
            total += test_value
    return total

def part_two(lines):
    total = 0
    for line in lines:
        if not line.strip():
            continue
        test_value, numbers = parse_equation(line)
        if can_produce_value(test_value, numbers, ['+', '*', '||']):
            total += test_value
    return total

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
