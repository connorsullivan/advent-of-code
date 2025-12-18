import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Count how many times the dial ends pointing at 0 after a rotation."""
    position = 50
    count = 0
    
    for line in lines:
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
    """Count how many times the dial points at 0 during AND after rotations."""
    position = 50
    count = 0
    
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        
        # Count zeros crossed during the rotation
        if direction == 'L':
            # Going left from position for distance clicks
            for _ in range(distance):
                position = (position - 1) % 100
                if position == 0:
                    count += 1
        else:  # R
            # Going right from position for distance clicks
            for _ in range(distance):
                position = (position + 1) % 100
                if position == 0:
                    count += 1
    
    return count

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
