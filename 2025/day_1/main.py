import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Count number of times dial ends on 0 after each rotation."""
    position = 50
    count = 0
    
    for line in lines:
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100
        
        if position == 0:
            count += 1
    
    return count

def part_two(lines):
    """Count all times dial passes through or lands on 0 during rotations."""
    position = 50
    count = 0
    
    for line in lines:
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            new_position = (position - distance) % 100
            # Full rotations through 0
            full_rotations = distance // 100
            count += full_rotations
            
            # Partial rotation: we hit 0 if we wrap around
            # Moving left by 'remaining' from 'position', we visit 0 if:
            # - remaining >= position (we reach or pass 0)
            # - But only if position > 0 (if we start at 0, we don't count it)
            remaining = distance % 100
            if remaining > 0 and position > 0 and remaining >= position:
                count += 1
            
            position = new_position
        else:  # R
            new_position = (position + distance) % 100
            # Full rotations through 0
            full_rotations = distance // 100
            count += full_rotations
            
            # Partial rotation: we hit 0 if position + remaining >= 100
            remaining = distance % 100
            if remaining > 0 and position + remaining >= 100:
                count += 1
            
            position = new_position
    
    return count

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
