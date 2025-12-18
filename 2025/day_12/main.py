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

def get_shape_coords(pattern):
    """Get relative coordinates of a shape."""
    coords = []
    for r, row in enumerate(pattern):
        for c, char in enumerate(row):
            if char == '#':
                coords.append((r, c))
    return coords

def get_all_orientations(coords):
    """Get all unique rotations and reflections of a shape."""
    orientations = set()
    
    current = list(coords)
    for _ in range(4):
        min_r = min(c[0] for c in current)
        min_c = min(c[1] for c in current)
        normalized = tuple(sorted((r - min_r, c - min_c) for r, c in current))
        orientations.add(normalized)
        
        flipped = [(-r, c) for r, c in current]
        min_r = min(c[0] for c in flipped)
        min_c = min(c[1] for c in flipped)
        normalized = tuple(sorted((r - min_r, c - min_c) for r, c in flipped))
        orientations.add(normalized)
        
        current = [(c, -r) for r, c in current]
    
    return list(orientations)

def get_placements(orientations, width, height):
    """Get all valid placements for a shape in a grid."""
    placements = []
    for coords in orientations:
        max_r = max(r for r, c in coords)
        max_c = max(c for r, c in coords)
        for r_off in range(height - max_r):
            for c_off in range(width - max_c):
                placement = frozenset((r + r_off, c + c_off) for r, c in coords)
                placements.append(placement)
    return placements

def solve_dlx(width, height, all_placements, remaining_shapes, covered, depth=0):
    """Solve using backtracking with better pruning."""
    # If no more shapes to place, success
    if not remaining_shapes:
        return True
    
    # Find the first uncovered cell (most constrained first)
    first_uncovered = None
    for r in range(height):
        for c in range(width):
            if (r, c) not in covered:
                first_uncovered = (r, c)
                break
        if first_uncovered:
            break
    
    # If all cells that could be covered by remaining shapes are covered, but we still have shapes, fail
    if first_uncovered is None:
        # Check if we still have shapes to place
        return not remaining_shapes
    
    # Get the shape with fewest valid placements covering the first uncovered cell
    best_shape = None
    best_count = float('inf')
    best_placements = []
    
    for shape_id, count in remaining_shapes.items():
        if count == 0:
            continue
        valid = [p for p in all_placements[shape_id] if first_uncovered in p and not (p & covered)]
        if len(valid) < best_count:
            best_count = len(valid)
            best_shape = shape_id
            best_placements = valid
    
    if best_shape is None or best_count == 0:
        return False
    
    for placement in best_placements:
        new_covered = covered | placement
        new_remaining = remaining_shapes.copy()
        new_remaining[best_shape] -= 1
        if new_remaining[best_shape] == 0:
            del new_remaining[best_shape]
        
        if solve_dlx(width, height, all_placements, new_remaining, new_covered, depth + 1):
            return True
    
    return False

def can_fit(width, height, counts, shapes):
    """Check if the presents can fit in the region."""
    # Get all shape orientations and placements
    all_placements = {}
    total_cells = 0
    remaining = {}
    
    for shape_id, count in enumerate(counts):
        if count > 0:
            pattern = shapes[shape_id]
            coords = get_shape_coords(pattern)
            orientations = get_all_orientations(coords)
            placements = get_placements(orientations, width, height)
            all_placements[shape_id] = placements
            remaining[shape_id] = count
            total_cells += len(coords) * count
    
    # Quick check: total cells must fit
    if total_cells > width * height:
        return False
    
    # No shapes to place
    if not remaining:
        return True
    
    return solve_dlx(width, height, all_placements, remaining, frozenset())

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
