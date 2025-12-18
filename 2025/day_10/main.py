import sys
import os
import re
from itertools import combinations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_line(line):
    """Parse a machine description."""
    # Extract indicator lights pattern
    lights_match = re.search(r'\[([.#]+)\]', line)
    lights_pattern = lights_match.group(1) if lights_match else ""
    
    # Extract button wirings
    buttons = []
    for m in re.finditer(r'\(([0-9,]+)\)', line):
        indices = tuple(int(x) for x in m.group(1).split(','))
        buttons.append(indices)
    
    # Extract joltage requirements
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    joltage = tuple(int(x) for x in joltage_match.group(1).split(',')) if joltage_match else ()
    
    return lights_pattern, buttons, joltage

def solve_lights(pattern, buttons):
    """Find minimum button presses to configure indicator lights."""
    n = len(pattern)
    target = tuple(1 if c == '#' else 0 for c in pattern)
    
    # For toggle-based problems, pressing a button twice is same as not pressing
    # So we only need to consider 0 or 1 presses per button
    min_presses = float('inf')
    num_buttons = len(buttons)
    
    for num_pressed in range(num_buttons + 1):
        for combo in combinations(range(num_buttons), num_pressed):
            state = [0] * n
            for btn_idx in combo:
                for light_idx in buttons[btn_idx]:
                    if light_idx < n:
                        state[light_idx] ^= 1
            if tuple(state) == target:
                min_presses = min(min_presses, num_pressed)
                break
    
    return min_presses if min_presses != float('inf') else 0

def solve_joltage(buttons, joltage):
    """Find minimum button presses using ILP."""
    n_counters = len(joltage)
    n_buttons = len(buttons)
    
    if n_buttons == 0 or n_counters == 0:
        return 0
    
    # Build constraint matrix A where A[j][i] = 1 if button i affects counter j
    A_eq = np.zeros((n_counters, n_buttons))
    for btn_idx, btn in enumerate(buttons):
        for counter_idx in btn:
            if counter_idx < n_counters:
                A_eq[counter_idx][btn_idx] = 1
    
    b_eq = np.array(list(joltage))
    c = np.ones(n_buttons)  # Minimize sum of presses
    
    # Use MILP with integer constraints
    integrality = np.ones(n_buttons)
    max_val = max(joltage) * 2 if joltage else 100
    bounds = Bounds(lb=np.zeros(n_buttons), ub=np.full(n_buttons, max_val))
    constraints = LinearConstraint(A_eq, b_eq, b_eq)
    
    result = milp(c, constraints=constraints, integrality=integrality, bounds=bounds)
    
    if result.success:
        return int(round(sum(result.x)))
    return 0

def part_one(lines):
    """Find minimum button presses for indicator lights."""
    total = 0
    for line in lines:
        if not line:
            continue
        pattern, buttons, _ = parse_line(line)
        presses = solve_lights(pattern, buttons)
        total += presses
    return total

def part_two(lines):
    """Find minimum button presses for joltage counters."""
    total = 0
    for line in lines:
        if not line:
            continue
        _, buttons, joltage = parse_line(line)
        presses = solve_joltage(buttons, joltage)
        total += presses
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
