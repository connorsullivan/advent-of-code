import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    graph = {}
    for line in lines:
        if not line:
            continue
        src, rest = line.split(":")
        neighbors = rest.strip().split()
        graph[src.strip()] = neighbors

    memo = {}
    target = "out"

    def dfs(node):
        if node == target:
            return 1
        if node in memo:
            return memo[node]
        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt)
        memo[node] = total
        return total

    return dfs("you")

def part_two(lines):
    graph = {}
    for line in lines:
        if not line:
            continue
        src, rest = line.split(":")
        neighbors = rest.strip().split()
        graph[src.strip()] = neighbors

    memo = {}
    target = "out"
    needed = {"dac", "fft"}

    def dfs(node, seen_dac, seen_fft):
        key = (node, seen_dac, seen_fft)
        if key in memo:
            return memo[key]
        if node == target:
            return 1 if (seen_dac and seen_fft) else 0
        new_dac = seen_dac or node == "dac"
        new_fft = seen_fft or node == "fft"
        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt, new_dac, new_fft)
        memo[key] = total
        return total

    return dfs("svr", False, False)

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
