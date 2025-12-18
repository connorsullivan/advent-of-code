import sys
import os
from typing import Iterable

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def _parse_points(lines: Iterable[str]) -> list[tuple[int, int]]:
    pts: list[tuple[int, int]] = []
    for line in lines:
        if not line:
            continue
        x, y = (int(p) for p in line.split(","))
        pts.append((x, y))
    return pts


def _edges(points: list[tuple[int, int]]) -> list[tuple[int, int, int, int]]:
    edges: list[tuple[int, int, int, int]] = []
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        edges.append((x1, y1, x2, y2))
    return edges


def _point_in_poly(point: tuple[int, int], edges: list[tuple[int, int, int, int]]) -> bool:
    x, y = point
    crossings = 0
    for x1, y1, x2, y2 in edges:
        if x1 == x2:  # vertical
            xv = x1
            ylo, yhi = (y1, y2) if y1 < y2 else (y2, y1)
            if x == xv and ylo <= y <= yhi:
                return True
            if x < xv and ylo <= y < yhi:
                crossings ^= 1
        else:  # horizontal
            yh = y1
            xlo, xhi = (x1, x2) if x1 < x2 else (x2, x1)
            if y == yh and xlo <= x <= xhi:
                return True
    return crossings == 1


def _boundary_intersects_open_rect(
    edges: list[tuple[int, int, int, int]],
    minx: int,
    maxx: int,
    miny: int,
    maxy: int,
) -> bool:
    if minx >= maxx or miny >= maxy:
        return False
    for x1, y1, x2, y2 in edges:
        if x1 == x2:  # vertical
            xv = x1
            if not (minx < xv < maxx):
                continue
            ylo, yhi = (y1, y2) if y1 < y2 else (y2, y1)
            if max(ylo, miny) < min(yhi, maxy):
                return True
        else:  # horizontal
            yh = y1
            if not (miny < yh < maxy):
                continue
            xlo, xhi = (x1, x2) if x1 < x2 else (x2, x1)
            if max(xlo, minx) < min(xhi, maxx):
                return True
    return False


def _segment_ok(
    edges: list[tuple[int, int, int, int]],
    a: tuple[int, int],
    b: tuple[int, int],
) -> bool:
    (x1, y1), (x2, y2) = a, b
    if x1 == x2:
        x = x1
        lo, hi = (y1, y2) if y1 < y2 else (y2, y1)
        mid = (x, (lo + hi) // 2)
        if not _point_in_poly(mid, edges):
            return False
        for ex1, ey1, ex2, ey2 in edges:
            if ey1 != ey2:
                continue
            yh = ey1
            if not (lo < yh < hi):
                continue
            xlo, xhi = (ex1, ex2) if ex1 < ex2 else (ex2, ex1)
            if xlo <= x <= xhi:
                return False
        return True
    if y1 == y2:
        y = y1
        lo, hi = (x1, x2) if x1 < x2 else (x2, x1)
        mid = ((lo + hi) // 2, y)
        if not _point_in_poly(mid, edges):
            return False
        for ex1, ey1, ex2, ey2 in edges:
            if ex1 != ex2:
                continue
            xv = ex1
            if not (lo < xv < hi):
                continue
            ylo, yhi = (ey1, ey2) if ey1 < ey2 else (ey2, ey1)
            if ylo <= y <= yhi:
                return False
        return True
    raise ValueError("Expected axis-aligned segment")


def part_one(lines):
    pts = _parse_points(lines)
    best = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        for j in range(i + 1, len(pts)):
            x2, y2 = pts[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > best:
                best = area
    return best

def part_two(lines):
    pts = _parse_points(lines)
    edges = _edges(pts)
    best = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        for j in range(i + 1, len(pts)):
            x2, y2 = pts[j]
            minx, maxx = (x1, x2) if x1 < x2 else (x2, x1)
            miny, maxy = (y1, y2) if y1 < y2 else (y2, y1)
            other1 = (x1, y2)
            other2 = (x2, y1)

            if minx == maxx and miny == maxy:
                best = max(best, 1)
                continue

            if minx == maxx:
                if _segment_ok(edges, (minx, miny), (minx, maxy)) and _point_in_poly(other1, edges):
                    best = max(best, maxy - miny + 1)
                continue

            if miny == maxy:
                if _segment_ok(edges, (minx, miny), (maxx, miny)) and _point_in_poly(other1, edges):
                    best = max(best, maxx - minx + 1)
                continue

            if not _point_in_poly(other1, edges) or not _point_in_poly(other2, edges):
                continue
            if _boundary_intersects_open_rect(edges, minx, maxx, miny, maxy):
                continue
            best = max(best, (maxx - minx + 1) * (maxy - miny + 1))
    return best

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
