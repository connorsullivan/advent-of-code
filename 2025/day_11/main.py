import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def parse_graph(lines):
    graph = {}
    for line in lines:
        if not line.strip():
            continue
        parts = line.split(':')
        node = parts[0].strip()
        outputs = parts[1].strip().split()
        graph[node] = outputs
    return graph

def count_paths(graph, start, end, memo):
    if start == end:
        return 1
    if start not in graph:
        return 0
    state = (start, end)
    if state in memo:
        return memo[state]

    total = 0
    for neighbor in graph[start]:
        total += count_paths(graph, neighbor, end, memo)

    memo[state] = total
    return total

def part_one(lines):
    graph = parse_graph(lines)
    memo = {}
    return count_paths(graph, 'you', 'out', memo)

def part_two(lines):
    graph = parse_graph(lines)
    memo = {}

    p_svr_dac = count_paths(graph, 'svr', 'dac', memo)
    p_dac_fft = count_paths(graph, 'dac', 'fft', memo)
    p_fft_out = count_paths(graph, 'fft', 'out', memo)

    p_svr_fft = count_paths(graph, 'svr', 'fft', memo)
    p_fft_dac = count_paths(graph, 'fft', 'dac', memo)
    p_dac_out = count_paths(graph, 'dac', 'out', memo)

    return p_svr_dac * p_dac_fft * p_fft_out + p_svr_fft * p_fft_dac * p_dac_out

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
