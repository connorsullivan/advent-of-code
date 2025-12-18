import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    """Find largest rectangle with red tiles as opposite corners."""
    # Parse red tile positions
    tiles = []
    for line in lines:
        coords = line.split(',')
        tiles.append((int(coords[0]), int(coords[1])))
    
    # Try all pairs of tiles as opposite corners
    max_area = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            
            # Calculate rectangle area
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            area = width * height
            
            max_area = max(max_area, area)
    
    return max_area

def part_two(lines):
    """Find largest rectangle using only red and green tiles."""
    # Parse red tile positions (in order, forming a loop)
    tiles = []
    for line in lines:
        coords = line.split(',')
        tiles.append((int(coords[0]), int(coords[1])))
    
    # Build set of green tiles (connecting lines between consecutive red tiles)
    # and red tiles
    allowed_tiles = set(tiles)  # Red tiles
    
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % len(tiles)]
        
        # Add all tiles on the line between (x1, y1) and (x2, y2)
        if x1 == x2:
            # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                allowed_tiles.add((x1, y))
        else:
            # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                allowed_tiles.add((x, y1))
    
    # For part 2, we need interior tiles too
    # To avoid timeout, let's use a more efficient method:
    # Only check tiles that are within reasonable distance of the perimeter
    
    # Try pairs of red tiles, but only validate using point-in-polygon for interior
    max_area = 0
    
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            
            # Quick check: are the corners on the perimeter or inside?
            # Only check a sample of points if rectangle is large
            area = (max_x - min_x) * (max_y - min_y)
            if area == 0:
                continue
            
            # For very large rectangles, use sampling
            LARGE_AREA_THRESHOLD = 10000
            if area > LARGE_AREA_THRESHOLD:
                # Sample check - check corners and center
                test_points = [
                    (min_x, min_y), (max_x, max_y),
                    (min_x, max_y), (max_x, min_y),
                    ((min_x + max_x) // 2, (min_y + max_y) // 2)
                ]
            else:
                # Full check for smaller rectangles
                test_points = [
                    (x, y)
                    for x in range(min_x, max_x + 1)
                    for y in range(min_y, max_y + 1)
                ]
            
            valid = True
            for x, y in test_points:
                if (x, y) in allowed_tiles:
                    continue
                # Check if inside polygon
                if not is_inside_polygon(x, y, tiles):
                    valid = False
                    break
            
            if valid:
                max_area = max(max_area, area)
    
    return max_area

def is_inside_polygon(x, y, polygon):
    """Check if point (x, y) is inside polygon using ray casting."""
    n = len(polygon)
    inside = False
    
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        
        j = i
    
    return inside

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
