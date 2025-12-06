import sys
import os
from functools import cmp_to_key

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    rules = []
    updates = []
    is_rules_section = True
    for line in lines:
        # lines are already stripped by read_input
        if not line:
            is_rules_section = False
            continue

        if is_rules_section:
            parts = line.split('|')
            rules.append((int(parts[0]), int(parts[1])))
        else:
            updates.append([int(x) for x in line.split(',')])
    return rules, updates

def is_ordered(update, rules_set):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            # Check if there is a rule saying the later element should be before the earlier element
            if (update[j], update[i]) in rules_set:
                return False
    return True

def part_one(lines):
    rules, updates = parse_input(lines)
    rules_set = set(rules)
    total = 0
    for update in updates:
        if is_ordered(update, rules_set):
            middle_index = len(update) // 2
            total += update[middle_index]
    return total

def compare_pages(a, b, rules_set):
    if (a, b) in rules_set:
        return -1
    if (b, a) in rules_set:
        return 1
    return 0

def part_two(lines):
    rules, updates = parse_input(lines)
    rules_set = set(rules)
    total = 0
    for update in updates:
        if not is_ordered(update, rules_set):
            sorted_update = sorted(update, key=cmp_to_key(lambda x, y: compare_pages(x, y, rules_set)))
            middle_index = len(sorted_update) // 2
            total += sorted_update[middle_index]
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
