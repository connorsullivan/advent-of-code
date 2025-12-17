import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    points = []
    for line in lines:
        if not line.strip():
            continue
        x, y = map(int, line.split(','))
        points.append((x, y))

    max_area = 0
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area:
                max_area = area
    return max_area

def part_two(lines):
    points = []
    for line in lines:
        if not line.strip():
            continue
        x, y = map(int, line.split(','))
        points.append((x, y))

    X = sorted(list(set(p[0] for p in points)))
    Y = sorted(list(set(p[1] for p in points)))
    x_map = {x: i for i, x in enumerate(X)}
    y_map = {y: j for j, y in enumerate(Y)}

    nx, ny = len(X), len(Y)
    is_inside = [[False] * (ny - 1) for _ in range(nx - 1)]

    for j in range(ny - 1):
        y_mid = (Y[j] + Y[j+1]) / 2
        vertical_edges_x = []
        for k in range(len(points)):
            p1 = points[k]
            p2 = points[(k + 1) % len(points)]
            if p1[0] == p2[0]: # Vertical edge
                if min(p1[1], p2[1]) <= y_mid <= max(p1[1], p2[1]):
                    vertical_edges_x.append(p1[0])
        vertical_edges_x.sort()
        for k in range(0, len(vertical_edges_x), 2):
            x_start = vertical_edges_x[k]
            x_end = vertical_edges_x[k+1]
            i_start = x_map[x_start]
            i_end = x_map[x_end]
            for i in range(i_start, i_end):
                is_inside[i][j] = True

    prefix_sum = [[0] * ny for _ in range(nx)]
    for i in range(nx - 1):
        for j in range(ny - 1):
            prefix_sum[i+1][j+1] = (1 if is_inside[i][j] else 0) \
                                   + prefix_sum[i][j+1] \
                                   + prefix_sum[i+1][j] \
                                   - prefix_sum[i][j]

    # Precompute which segments are okay for line rectangles
    v_seg_ok = [[False] * (ny - 1) for _ in range(nx)]
    for i in range(nx):
        for j in range(ny - 1):
            ok = False
            if i > 0 and is_inside[i-1][j]: ok = True
            if i < nx - 1 and is_inside[i][j]: ok = True
            v_seg_ok[i][j] = ok

    h_seg_ok = [[False] * (nx - 1) for _ in range(ny)]
    for j in range(ny):
        for i in range(nx - 1):
            ok = False
            if j > 0 and is_inside[i][j-1]: ok = True
            if j < ny - 1 and is_inside[i][j]: ok = True
            h_seg_ok[j][i] = ok

    v_seg_prefix = [[0] * ny for _ in range(nx)]
    for i in range(nx):
        for j in range(ny - 1):
            v_seg_prefix[i][j+1] = v_seg_prefix[i][j] + (1 if v_seg_ok[i][j] else 0)

    h_seg_prefix = [[0] * nx for _ in range(ny)]
    for j in range(ny):
        for i in range(nx - 1):
            h_seg_prefix[j][i+1] = h_seg_prefix[j][i] + (1 if h_seg_ok[j][i] else 0)

    max_area = 0
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            ix1, ix2 = sorted([x_map[x1], x_map[x2]])
            iy1, iy2 = sorted([y_map[y1], y_map[y2]])

            if ix1 < ix2 and iy1 < iy2:
                num_cells = (ix2 - ix1) * (iy2 - iy1)
                actual_cells = prefix_sum[ix2][iy2] - prefix_sum[ix1][iy2] - prefix_sum[ix2][iy1] + prefix_sum[ix1][iy1]
                if actual_cells == num_cells:
                    area = (X[ix2] - X[ix1] + 1) * (Y[iy2] - Y[iy1] + 1)
                    if area > max_area:
                        max_area = area
            elif ix1 == ix2 and iy1 < iy2:
                # Vertical line
                num_segs = iy2 - iy1
                actual_segs = v_seg_prefix[ix1][iy2] - v_seg_prefix[ix1][iy1]
                if actual_segs == num_segs:
                    area = 1 * (Y[iy2] - Y[iy1] + 1)
                    if area > max_area:
                        max_area = area
            elif iy1 == iy2 and ix1 < ix2:
                # Horizontal line
                num_segs = ix2 - ix1
                actual_segs = h_seg_prefix[iy1][ix2] - h_seg_prefix[iy1][ix1]
                if actual_segs == num_segs:
                    area = (X[ix2] - X[ix1] + 1) * 1
                    if area > max_area:
                        max_area = area
            else:
                # Single point
                area = 1
                if area > max_area:
                    max_area = area

    return max_area

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
