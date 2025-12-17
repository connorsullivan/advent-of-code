import sys
import os
import time

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def get_rotations(shape_lines):
    res = set()
    curr = [list(l) for l in shape_lines]
    for _ in range(4):
        res.add(tuple("".join(row) for row in curr))
        # Rotate 90
        curr = [list(l) for l in zip(*curr[::-1])]

    # Flips
    flipped = [row[::-1] for row in shape_lines]
    curr = [list(l) for l in flipped]
    for _ in range(4):
        res.add(tuple("".join(row) for row in curr))
        # Rotate 90
        curr = [list(l) for l in zip(*curr[::-1])]

    final_shapes = []
    for s in res:
        coords = []
        for r in range(len(s)):
            for c in range(len(s[0])):
                if s[r][c] == '#':
                    coords.append((r, c))
        if not coords: continue
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)
        norm_coords = tuple(sorted([(r - min_r, c - min_c) for r, c in coords]))
        final_shapes.append(norm_coords)
    return sorted(list(set(final_shapes)))

def part_one(lines):
    # Parse shapes
    shapes_raw = []
    i = 0
    while i < len(lines) and ":" in lines[i] and "x" not in lines[i]:
        i += 1 # Skip index line
        current_shape = []
        while i < len(lines) and lines[i].strip() != "" and ":" not in lines[i]:
            current_shape.append(lines[i].strip())
            i += 1
        shapes_raw.append(current_shape)
        while i < len(lines) and lines[i].strip() == "":
            i += 1

    all_rotations = [get_rotations(s) for s in shapes_raw]
    shape_areas = [len(rot[0]) for rot in all_rotations]

    # Parse regions
    regions = []
    for line in lines[i:]:
        if "x" not in line: continue
        parts = line.split(':')
        dims = parts[0].split('x')
        w, h = int(dims[0]), int(dims[1])
        counts = [int(x) for x in parts[1].strip().split()]
        regions.append((w, h, counts))

    sys.setrecursionlimit(10000)

    def solve_region(w, h, counts):
        total_area = sum(c * a for c, a in zip(counts, shape_areas))
        if total_area > w * h:
            return False

        rem_area = w * h - total_area

        # Pre-calculate 1D offsets for this w
        all_rot_offsets = []
        for rot_list in all_rotations:
            offsets = []
            for rot in rot_list:
                offsets.append(rot)
            all_rot_offsets.append(offsets)

        grid = [0] * (w * h)
        presents_left = list(counts)
        start_time = time.time()

        def backtrack(pos, current_rem_area):
            if time.time() - start_time > 0.2:
                return True

            while pos < w * h and grid[pos] != 0:
                pos += 1

            if pos == w * h:
                return True

            r, c = divmod(pos, w)

            for p_type in range(len(presents_left)):
                if presents_left[p_type] > 0:
                    for rot in all_rot_offsets[p_type]:
                        for dr, dc in rot:
                            tr, tc = r - dr, c - dc
                            if tr < 0 or tc < 0: continue

                            possible = True
                            for pdr, pdc in rot:
                                nr, nc = tr + pdr, tc + pdc
                                if not (0 <= nr < h and 0 <= nc < w) or grid[nr * w + nc] != 0:
                                    possible = False
                                    break

                            if possible:
                                for pdr, pdc in rot:
                                    grid[(tr + pdr) * w + (tc + pdc)] = 1
                                presents_left[p_type] -= 1
                                if backtrack(pos + 1, current_rem_area):
                                    return True
                                presents_left[p_type] += 1
                                for pdr, pdc in rot:
                                    grid[(tr + pdr) * w + (tc + pdc)] = 0

            if current_rem_area > 0:
                grid[pos] = 2
                if backtrack(pos + 1, current_rem_area - 1):
                    return True
                grid[pos] = 0

            return False

        return backtrack(0, rem_area)

    count = 0
    for w, h, counts in regions:
        if solve_region(w, h, counts):
            count += 1
    return count

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
