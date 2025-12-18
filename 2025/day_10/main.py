import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input
import re
from fractions import Fraction

def parse_line(line):
    pattern = re.search(r"\[([.#]+)\]", line).group(1)
    buttons = [grp for grp in re.findall(r"\(([^)]*)\)", line)]
    targets = re.search(r"\{([^}]*)\}", line).group(1)
    return pattern, buttons, targets

def part_one(lines):
    best_total = 0
    for line in lines:
        if not line:
            continue
        pattern, buttons_raw, _ = parse_line(line)
        lights = len(pattern)
        target_mask = 0
        for idx, ch in enumerate(pattern):
            if ch == "#":
                target_mask |= 1 << idx
        button_masks = []
        for b in buttons_raw:
            indices = [int(x) for x in b.split(",") if x]
            mask = 0
            for idx in indices:
                mask |= 1 << idx
            button_masks.append(mask)
        min_presses = None
        combos = 1 << len(button_masks)
        for combo in range(combos):
            state = 0
            presses = 0
            for i, mask in enumerate(button_masks):
                if combo >> i & 1:
                    state ^= mask
                    presses += 1
            if state == target_mask:
                if min_presses is None or presses < min_presses:
                    min_presses = presses
                    if min_presses == 0:
                        break
        best_total += min_presses if min_presses is not None else 0
    return best_total

def part_two(lines):
    total = 0
    for line in lines:
        if not line:
            continue
        _, buttons_raw, targets_raw = parse_line(line)
        targets = [int(x) for x in targets_raw.split(",") if x.strip()]
        counters = len(targets)
        button_vectors = []
        for b in buttons_raw:
            vec = [0] * counters
            if b.strip():
                for idx in b.split(","):
                    if idx:
                        vec[int(idx)] = 1
            button_vectors.append(tuple(vec))
        button_vectors = list(dict.fromkeys(button_vectors))
        button_vectors = [v for v in button_vectors if any(v)]
        buttons = len(button_vectors)
        if buttons == 0:
            total += 0
            continue

        # Build matrix (counters x buttons)
        mat = [[Fraction(button_vectors[b][c]) for b in range(buttons)] for c in range(counters)]
        for i in range(counters):
            mat[i].append(Fraction(targets[i]))

        rows = counters
        cols = buttons
        pivot_cols = []
        r = 0
        for c in range(cols):
            pivot_row = None
            for rr in range(r, rows):
                if mat[rr][c] != 0:
                    pivot_row = rr
                    break
            if pivot_row is None:
                continue
            mat[r], mat[pivot_row] = mat[pivot_row], mat[r]
            pivot = mat[r][c]
            for cc in range(c, cols + 1):
                mat[r][cc] /= pivot
            for rr in range(rows):
                if rr != r and mat[rr][c] != 0:
                    factor = mat[rr][c]
                    for cc in range(c, cols + 1):
                        mat[rr][cc] -= factor * mat[r][cc]
            pivot_cols.append(c)
            r += 1
            if r == rows:
                break

        # Check consistency
        inconsistent = False
        for rr in range(rows):
            if all(mat[rr][cc] == 0 for cc in range(cols)) and mat[rr][cols] != 0:
                inconsistent = True
                break
        if inconsistent:
            total += 0
            continue
        else:
            pivot_set = set(pivot_cols)
            free_cols = [c for c in range(cols) if c not in pivot_set]

            max_press = []
            for b in range(buttons):
                affected = [targets[i] for i in range(counters) if button_vectors[b][i]]
                max_press.append(min(affected) if affected else 0)

            def eval_pivots(free_vals):
                values = [0] * cols
                for idx, fc in enumerate(free_cols):
                    values[fc] = free_vals[idx]
                for row_idx, pc in enumerate(pivot_cols):
                    rhs = mat[row_idx][cols]
                    for idx, fc in enumerate(free_cols):
                        rhs -= mat[row_idx][fc] * free_vals[idx]
                    if rhs.denominator != 1:
                        return None
                    val = rhs.numerator
                    if val < 0 or val > max_press[pc]:
                        return None
                    values[pc] = val
                return values

            best = None
            if not free_cols:
                vals = eval_pivots([])
                if vals is not None:
                    best = sum(vals)
            else:
                bounds = [max_press[fc] for fc in free_cols]
                def dfs(idx, acc, partial_sum):
                    nonlocal best
                    if idx == len(free_cols):
                        vals = eval_pivots(acc)
                        if vals is None:
                            return
                        cost = sum(vals)
                        if best is None or cost < best:
                            best = cost
                        return
                    limit = bounds[idx]
                    for v in range(limit + 1):
                        if best is not None and partial_sum + v >= best:
                            break
                        dfs(idx + 1, acc + [v], partial_sum + v)
                dfs(0, [], 0)
            total += best if best is not None else 0
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
