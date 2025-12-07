import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
from functools import cmp_to_key

def parse_input(lines):
    """Parse the input into rules and updates."""
    rules = []
    updates = []

    parsing_rules = True
    for line in lines:
        line = line.strip()
        if not line:
            parsing_rules = False
            continue

        if parsing_rules:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
        else:
            updates.append(list(map(int, line.split(','))))

    return rules, updates

def is_valid_order(update, rules):
    """Check if an update is in valid order according to the rules."""
    # Create a position map for quick lookup
    position = {page: i for i, page in enumerate(update)}

    # Check each rule
    for x, y in rules:
        # Only check if both pages are in the update
        if x in position and y in position:
            # x must come before y
            if position[x] > position[y]:
                return False

    return True

def sort_update(update, rules):
    """Sort an update according to the rules."""
    # Create a comparison function based on the rules
    def compare(a, b):
        # Check if there's a rule a|b (a should come before b)
        for x, y in rules:
            if x == a and y == b:
                return -1  # a comes before b
            if x == b and y == a:
                return 1   # b comes before a
        return 0  # no rule applies

    # Sort the update using the comparison function
    return sorted(update, key=cmp_to_key(compare))

def part_one(lines):
    """Find correctly ordered updates and sum their middle page numbers."""
    rules, updates = parse_input(lines)

    total = 0
    for update in updates:
        if is_valid_order(update, rules):
            # Get the middle page number
            middle_idx = len(update) // 2
            total += update[middle_idx]

    return total

def part_two(lines):
    """Fix incorrectly ordered updates and sum their middle page numbers."""
    rules, updates = parse_input(lines)

    total = 0
    for update in updates:
        if not is_valid_order(update, rules):
            # Sort the incorrectly ordered update
            sorted_update = sort_update(update, rules)
            # Get the middle page number
            middle_idx = len(sorted_update) // 2
            total += sorted_update[middle_idx]

    return total

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
