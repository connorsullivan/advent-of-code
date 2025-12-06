import sys
import os
from functools import lru_cache
from itertools import permutations

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

# Coordinates
NUMPAD = {
    '7': (0, 0), '8': (1, 0), '9': (2, 0),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '1': (0, 2), '2': (1, 2), '3': (2, 2),
    '0': (1, 3), 'A': (2, 3)
}
NUMPAD_GAP = (0, 3)

DIRPAD = {
    '^': (1, 0), 'A': (2, 0),
    '<': (0, 1), 'v': (1, 1), '>': (2, 1)
}
DIRPAD_GAP = (0, 0)

@lru_cache(None)
def get_paths(start, end, is_numpad):
    positions = NUMPAD if is_numpad else DIRPAD
    gap = NUMPAD_GAP if is_numpad else DIRPAD_GAP

    sx, sy = positions[start]
    ex, ey = positions[end]
    dx = ex - sx
    dy = ey - sy

    moves = []
    if dx > 0: moves.extend(['>'] * dx)
    if dx < 0: moves.extend(['<'] * -dx)
    if dy > 0: moves.extend(['v'] * dy)
    if dy < 0: moves.extend(['^'] * -dy)

    valid_paths = []
    seen = set()

    for p in permutations(moves):
        if p in seen: continue
        seen.add(p)

        cx, cy = sx, sy
        valid = True
        for move in p:
            if move == '>': cx += 1
            elif move == '<': cx -= 1
            elif move == 'v': cy += 1
            elif move == '^': cy -= 1

            if (cx, cy) == gap:
                valid = False
                break

        if valid:
            valid_paths.append("".join(p) + 'A')

    return valid_paths

# Memoization for costs
# cost_cache[depth][(start, end)] = min_len
cost_cache = {}

def get_dirpad_cost(start, end, depth):
    state = (start, end, depth)
    if state in cost_cache:
        return cost_cache[state]

    paths = get_paths(start, end, False)

    if depth == 0:
        # Base case: just the length of the move + 1 for 'A' (already included in get_paths)
        return len(paths[0])

    min_cost = float('inf')

    for path in paths:
        cost = 0
        current_key = 'A'
        for char in path:
            cost += get_dirpad_cost(current_key, char, depth - 1)
            current_key = char

        if cost < min_cost:
            min_cost = cost

    cost_cache[state] = min_cost
    return min_cost

def solve_code(code, depth):
    total_cost = 0
    current_key = 'A'

    for char in code:
        paths = get_paths(current_key, char, True)
        min_path_cost = float('inf')

        for path in paths:
            cost = 0
            dir_key = 'A'
            for p_char in path:
                cost += get_dirpad_cost(dir_key, p_char, depth - 1)
                dir_key = p_char

            if cost < min_path_cost:
                min_path_cost = cost

        total_cost += min_path_cost
        current_key = char

    return total_cost

def part_one(lines):
    total_complexity = 0
    for line in lines:
        line = line.strip()
        if not line: continue

        # Numeric part: remove leading zeros and 'A'
        # e.g. 029A -> 29
        numeric_part = int(line[:-1])

        # Part 1 has 2 directional keypads.
        length = solve_code(line, 2)
        total_complexity += length * numeric_part

    return total_complexity

def part_two(lines):
    total_complexity = 0
    for line in lines:
        line = line.strip()
        if not line: continue

        numeric_part = int(line[:-1])

        # Part 2 has 25 directional keypads.
        length = solve_code(line, 25)
        total_complexity += length * numeric_part

    return total_complexity

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
