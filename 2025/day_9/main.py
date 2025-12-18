import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_input(lines):
    """Parse red tile coordinates."""
    tiles = []
    for line in lines:
        if line:
            x, y = map(int, line.split(','))
            tiles.append((x, y))
    return tiles

def part_one(lines):
    """Find largest rectangle area using any two red tiles as opposite corners."""
    tiles = parse_input(lines)
    max_area = 0
    
    n = len(tiles)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            # Rectangle with opposite corners at (x1,y1) and (x2,y2)
            # Area includes both corners, so +1 on each dimension
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            max_area = max(max_area, area)
    
    return max_area

def part_two(lines):
    """Find largest rectangle using only red/green tiles."""
    tiles = parse_input(lines)
    n = len(tiles)
    
    red_set = set(tiles)
    
    # Precompute which edges are horizontal and which are vertical
    h_edges = []  # (y, x1, x2) where x1 <= x2
    v_edges = []  # (x, y1, y2) where y1 <= y2
    for i in range(n):
        p1 = tiles[i]
        p2 = tiles[(i + 1) % n]
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            v_edges.append((x1, min(y1, y2), max(y1, y2)))
        else:
            h_edges.append((y1, min(x1, x2), max(x1, x2)))
    
    def is_inside_or_on_boundary(x, y):
        """Check if point is inside or on the boundary of the polygon."""
        if (x, y) in red_set:
            return True
        
        # Check if on a vertical edge
        for ex, ey1, ey2 in v_edges:
            if x == ex and ey1 <= y <= ey2:
                return True
        
        # Check if on a horizontal edge
        for ey, ex1, ex2 in h_edges:
            if y == ey and ex1 <= x <= ex2:
                return True
        
        # Ray casting for interior
        crossings = 0
        for ex, ey1, ey2 in v_edges:
            if ex > x and ey1 <= y < ey2:
                crossings += 1
        return crossings % 2 == 1
    
    def is_rectangle_valid(min_x, max_x, min_y, max_y):
        """Check if rectangle is entirely within the polygon."""
        # Check 4 corners
        for x in [min_x, max_x]:
            for y in [min_y, max_y]:
                if not is_inside_or_on_boundary(x, y):
                    return False
        
        # Check if any vertical polygon edge crosses through the rectangle
        for ex, ey1, ey2 in v_edges:
            if min_x < ex < max_x:
                if ey1 < max_y and ey2 > min_y:
                    return False
        
        # Check if any horizontal polygon edge crosses through the rectangle
        for ey, ex1, ex2 in h_edges:
            if min_y < ey < max_y:
                if ex1 < max_x and ex2 > min_x:
                    return False
        
        # Check midpoints of each edge and center
        mid_x = (min_x + max_x) // 2
        mid_y = (min_y + max_y) // 2
        
        points_to_check = [
            (mid_x, min_y),
            (mid_x, max_y),
            (min_x, mid_y),
            (max_x, mid_y),
            (mid_x, mid_y),
        ]
        
        for x, y in points_to_check:
            if not is_inside_or_on_boundary(x, y):
                return False
        
        return True
    
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            
            min_rx, max_rx = min(x1, x2), max(x1, x2)
            min_ry, max_ry = min(y1, y2), max(y1, y2)
            
            if is_rectangle_valid(min_rx, max_rx, min_ry, max_ry):
                area = (max_rx - min_rx + 1) * (max_ry - min_ry + 1)
                max_area = max(max_area, area)
    
    return max_area

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
