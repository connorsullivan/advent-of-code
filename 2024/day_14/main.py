import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_robots(lines):
    """Parse robot positions and velocities from input lines."""
    robots = []
    for line in lines:
        if not line.strip():
            continue
        # Parse format: p=x,y v=vx,vy
        parts = line.strip().split()
        pos_part = parts[0][2:]  # Remove 'p='
        vel_part = parts[1][2:]  # Remove 'v='

        px, py = map(int, pos_part.split(','))
        vx, vy = map(int, vel_part.split(','))
        robots.append(((px, py), (vx, vy)))
    return robots

def simulate_robot(pos, vel, width, height, seconds):
    """Simulate a single robot for given seconds with wrapping."""
    px, py = pos
    vx, vy = vel

    # Calculate final position with wrapping
    final_x = (px + vx * seconds) % width
    final_y = (py + vy * seconds) % height

    return (final_x, final_y)

def count_quadrants(positions, width, height):
    """Count robots in each quadrant, ignoring middle lines."""
    mid_x = width // 2
    mid_y = height // 2

    quadrants = [0, 0, 0, 0]  # top-left, top-right, bottom-left, bottom-right

    for x, y in positions:
        # Skip robots exactly on middle lines
        if x == mid_x or y == mid_y:
            continue

        if x < mid_x and y < mid_y:
            quadrants[0] += 1  # top-left
        elif x > mid_x and y < mid_y:
            quadrants[1] += 1  # top-right
        elif x < mid_x and y > mid_y:
            quadrants[2] += 1  # bottom-left
        else:  # x > mid_x and y > mid_y
            quadrants[3] += 1  # bottom-right

    return quadrants

def part_one(lines):
    robots = parse_robots(lines)
    width = 101
    height = 103
    seconds = 100

    # Simulate all robots
    final_positions = []
    for pos, vel in robots:
        final_pos = simulate_robot(pos, vel, width, height, seconds)
        final_positions.append(final_pos)

    # Count quadrants
    quadrants = count_quadrants(final_positions, width, height)

    # Calculate safety factor
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    return safety_factor

def has_christmas_tree_pattern(positions, width, height):
    """
    Check if positions form a Christmas tree pattern.
    A Christmas tree likely has many robots clustered together forming a shape.
    We'll look for a large connected component or high density in a region.
    """
    pos_set = set(positions)

    # Check for long horizontal or diagonal lines which might indicate a tree
    # Count maximum consecutive robots in rows
    max_consecutive = 0
    for y in range(height):
        consecutive = 0
        for x in range(width):
            if (x, y) in pos_set:
                consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)
            else:
                consecutive = 0

    # A Christmas tree pattern would likely have at least 10+ consecutive robots in a row
    return max_consecutive >= 10

def visualize_robots(positions, width, height):
    """Create a visual representation of robot positions."""
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        grid[y][x] = '#'
    return '\n'.join(''.join(row) for row in grid)

def part_two(lines):
    robots = parse_robots(lines)
    width = 101
    height = 103

    # Search for the Christmas tree pattern
    # It should happen within a reasonable number of seconds
    for seconds in range(1, 10000):
        final_positions = []
        for pos, vel in robots:
            final_pos = simulate_robot(pos, vel, width, height, seconds)
            final_positions.append(final_pos)

        if has_christmas_tree_pattern(final_positions, width, height):
            # Optional: save visualization
            visualization = visualize_robots(final_positions, width, height)
            with open("tree_visualization.txt", "w") as f:
                f.write(f"Christmas tree at {seconds} seconds:\n")
                f.write(visualization)
            return seconds

    return -1  # Not found

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
