import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    points = [tuple(map(int, line.split(","))) for line in lines if line]
    max_area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            area = abs(x1 - x2) * abs(y1 - y2)
            if area > max_area:
                max_area = area
    return max_area

def part_two(lines):
    vertices = [tuple(map(int, line.split(","))) for line in lines if line]
    n = len(vertices)

    vertical_edges = []
    horizontal_by_y = {}
    vertical_by_x = {}
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        if x1 == x2:
            lo, hi = sorted((y1, y2))
            vertical_edges.append((x1, lo, hi))
            vertical_by_x.setdefault(x1, []).append((lo, hi))
        else:
            lo, hi = sorted((x1, x2))
            horizontal_by_y.setdefault(y1, []).append((lo, hi))

    y_queries = {y for _, y in vertices}
    crossings = {}
    for y in y_queries:
        xs = []
        for x, y_lo, y_hi in vertical_edges:
            if y_lo <= y < y_hi:
                xs.append(x)
        xs.sort()
        crossings[y] = xs

    def on_boundary(x, y):
        for lo, hi in horizontal_by_y.get(y, []):
            if lo <= x <= hi:
                return True
        for lo, hi in vertical_by_x.get(x, []):
            if lo <= y <= hi:
                return True
        return False

    def inside_or_boundary(x, y):
        if on_boundary(x, y):
            return True
        xs = crossings.get(y)
        if xs is None:
            return False
        cnt = 0
        for xv in xs:
            if xv > x:
                cnt += 1
        return cnt % 2 == 1

    max_area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        for j in range(i + 1, n):
            x2, y2 = vertices[j]
            if x1 == x2 or y1 == y2:
                continue
            area = abs(x1 - x2) * abs(y1 - y2)
            if area <= max_area:
                continue
            c1 = (x1, y2)
            c2 = (x2, y1)
            if inside_or_boundary(*c1) and inside_or_boundary(*c2):
                max_area = area
    return max_area

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
