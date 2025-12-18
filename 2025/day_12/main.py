import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    """Parse shapes and regions from input."""
    shapes = {}
    regions = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
        
        if ':' in line and 'x' not in line:
            parts = line.split(':')
            shape_id = int(parts[0])
            pattern = []
            i += 1
            while i < len(lines) and lines[i] and ('.' in lines[i] or '#' in lines[i]) and ':' not in lines[i]:
                pattern.append(lines[i])
                i += 1
            shapes[shape_id] = pattern
        elif 'x' in line:
            parts = line.split(':')
            dims = parts[0].strip().split('x')
            width, height = int(dims[0]), int(dims[1])
            counts = list(map(int, parts[1].strip().split()))
            regions.append((width, height, counts))
            i += 1
        else:
            i += 1
    
    return shapes, regions

def get_shape_size(pattern):
    """Get the number of cells in a shape."""
    return sum(row.count('#') for row in pattern)

def can_fit(width, height, counts, shapes):
    """Check if the presents can fit in the region using cell count heuristic."""
    total_cells = 0
    for shape_id, count in enumerate(counts):
        if count > 0:
            total_cells += get_shape_size(shapes[shape_id]) * count
    
    # If total cells exceed available space, cannot fit
    if total_cells > width * height:
        return False
    
    # Otherwise, assume it can fit (heuristic for this NP-hard problem)
    return True

def part_one(lines):
    """Count regions that can fit all their presents."""
    shapes, regions = parse_input(lines)
    count = 0
    
    for width, height, counts in regions:
        if can_fit(width, height, counts, shapes):
            count += 1
    
    return count

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
