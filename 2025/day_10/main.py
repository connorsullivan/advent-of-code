import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_machine(line):
    """Parse a machine specification line."""
    import re
    
    # Extract indicator lights
    lights_match = re.search(r'\[(.*?)\]', line)
    lights = [1 if c == '#' else 0 for c in lights_match.group(1)]
    
    # Extract button wiring
    buttons_text = re.findall(r'\(([\d,]+)\)', line)
    buttons = []
    for btn_text in buttons_text:
        indices = [int(x) for x in btn_text.split(',')]
        buttons.append(indices)
    
    # Extract joltage requirements
    joltage_match = re.search(r'\{([\d,]+)\}', line)
    joltages = [int(x) for x in joltage_match.group(1).split(',')]
    
    return lights, buttons, joltages

def solve_lights_gf2(target, buttons):
    """Solve system of equations in GF(2) to minimize button presses."""
    n_lights = len(target)
    n_buttons = len(buttons)
    
    # Build matrix: each button is a column, each light is a row
    # We want to find x (button presses) such that Ax = target (mod 2)
    
    # Try all possible combinations (brute force for small n)
    if n_buttons <= 20:
        min_presses = float('inf')
        for mask in range(1 << n_buttons):
            state = [0] * n_lights
            presses = 0
            for i in range(n_buttons):
                if mask & (1 << i):
                    presses += 1
                    for light_idx in buttons[i]:
                        state[light_idx] ^= 1
            
            if state == target:
                min_presses = min(min_presses, presses)
        
        return min_presses if min_presses != float('inf') else 0
    
    return 0  # Fallback

def solve_joltage_linear(target, buttons):
    """Solve linear system to minimize button presses for joltage."""
    n_counters = len(target)
    n_buttons = len(buttons)
    
    # Build coefficient matrix
    # button[j] affects counters listed in buttons[j]
    # If we press button j x_j times, counter i increases by (# of times j affects i) * x_j
    
    # Greedy approach: repeatedly press buttons that help most
    current = [0] * n_counters
    total_presses = 0
    
    max_iterations = 10000
    for _ in range(max_iterations):
        if current == target:
            break
        
        # Find which button to press
        best_button = -1
        best_score = -1
        
        for btn_idx, btn in enumerate(buttons):
            # Calculate how much this button helps
            score = 0
            for counter_idx in btn:
                if counter_idx < n_counters and current[counter_idx] < target[counter_idx]:
                    score += 1
            
            if score > best_score:
                best_score = score
                best_button = btn_idx
        
        if best_button == -1:
            break
        
        # Press the best button
        for counter_idx in buttons[best_button]:
            if counter_idx < n_counters:
                current[counter_idx] += 1
        total_presses += 1
    
    return total_presses

def part_one(lines):
    """Find minimum button presses to configure indicator lights."""
    total = 0
    for line in lines:
        lights, buttons, _ = parse_machine(line)
        presses = solve_lights_gf2(lights, buttons)
        total += presses
    return total

def part_two(lines):
    """Find minimum button presses to configure joltage counters."""
    total = 0
    for line in lines:
        _, buttons, joltages = parse_machine(line)
        presses = solve_joltage_linear(joltages, buttons)
        total += presses
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
