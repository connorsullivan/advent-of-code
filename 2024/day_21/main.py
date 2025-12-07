import sys
import os
from functools import lru_cache
from itertools import permutations

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

# Numeric keypad layout
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

NUMERIC_KEYPAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2)
}

# Directional keypad layout
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

DIRECTIONAL_KEYPAD = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

def get_moves(from_pos, to_pos, keypad):
    """Get all valid move sequences from one position to another."""
    from_r, from_c = from_pos
    to_r, to_c = to_pos

    dr = to_r - from_r
    dc = to_c - from_c

    # Build the move string
    moves = []
    if dr > 0:
        moves.extend(['v'] * dr)
    elif dr < 0:
        moves.extend(['^'] * (-dr))

    if dc > 0:
        moves.extend(['>'] * dc)
    elif dc < 0:
        moves.extend(['<'] * (-dc))

    if not moves:
        return ['A']  # Already at target

    # Generate all permutations of moves
    valid_sequences = []
    seen = set()

    for perm in permutations(moves):
        perm_str = ''.join(perm)
        if perm_str in seen:
            continue
        seen.add(perm_str)

        # Check if this path is valid (doesn't pass through the gap)
        r, c = from_r, from_c
        valid = True

        for move in perm:
            if move == '^':
                r -= 1
            elif move == 'v':
                r += 1
            elif move == '<':
                c -= 1
            elif move == '>':
                c += 1

            # Check if we hit the gap
            if keypad == 'numeric' and (r, c) == (3, 0):
                valid = False
                break
            elif keypad == 'directional' and (r, c) == (0, 0):
                valid = False
                break

        if valid:
            valid_sequences.append(perm_str + 'A')

    return valid_sequences if valid_sequences else ['A']

@lru_cache(maxsize=None)
def get_sequence_length(code, depth, max_depth):
    """
    Calculate the minimum button presses needed at the given depth.
    depth=0 means we're at the numeric keypad.
    depth=max_depth means we're typing directly.
    """
    if depth == max_depth:
        return len(code)

    # Determine which keypad we're using
    if depth == 0:
        keypad = NUMERIC_KEYPAD
        keypad_type = 'numeric'
    else:
        keypad = DIRECTIONAL_KEYPAD
        keypad_type = 'directional'

    total_length = 0
    current_pos = keypad['A']

    for char in code:
        target_pos = keypad[char]

        # Get all possible move sequences
        possible_sequences = get_moves(current_pos, target_pos, keypad_type)

        # For each possible sequence, calculate the cost at the next depth
        min_cost = float('inf')
        for seq in possible_sequences:
            cost = get_sequence_length(seq, depth + 1, max_depth)
            min_cost = min(min_cost, cost)

        total_length += min_cost
        current_pos = target_pos

    return total_length

def calculate_complexity(code, num_robots):
    """Calculate the complexity of a code with the given number of robots."""
    # num_robots includes the numeric keypad robot
    # So we have num_robots - 1 directional robots + 1 numeric robot
    sequence_length = get_sequence_length(code, 0, num_robots)
    numeric_value = int(code[:-1])  # Remove 'A' and convert to int
    return sequence_length * numeric_value

def part_one(lines):
    # Part 1: You + 2 directional robots + 1 numeric robot = 3 total robots
    total_complexity = 0
    for code in lines:
        code = code.strip()
        if code:
            complexity = calculate_complexity(code, 3)
            total_complexity += complexity
    return total_complexity

def part_two(lines):
    # Part 2: You + 25 directional robots + 1 numeric robot = 26 total robots
    total_complexity = 0
    for code in lines:
        code = code.strip()
        if code:
            complexity = calculate_complexity(code, 26)
            total_complexity += complexity
    return total_complexity

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
