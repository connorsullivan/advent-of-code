# Advent of Code

This repository contains Advent of Code puzzles, organized by year and day. The goal is to provide a structured environment for solving these coding challenges using Python.

## Project Structure

The project is organized into a root directory containing shared utilities and subdirectories for each year and day's puzzle.

### `utils/`

Contains shared library functions and helpers used across multiple days.

- `file_reader.py`: Functions for reading input files (e.g., `read_input`).

### `2024/day_X/` (e.g., `2024/day_1`, `2024/day_2`, ...)

Each day's directory contains the specific files for that day's puzzle:

- **`main.py`**: The main Python script for implementing the solution logic.
- It imports helper functions from `utils`.
- It defines `part_one(lines)` and `part_two(lines)` functions.
- It reads from `input.txt` and prints the results for both parts.
- **`input.txt`**: The raw puzzle input text file. This file often contains hundreds or even thousands of lines of data.
- **`part_1.txt`**: A text file containing the description and requirements for Part 1 of the puzzle.
- **`part_2.txt`**: A text file containing the description and requirements for Part 2 of the puzzle.
- **`discussion.md`**: A markdown file for explaining the reasoning and approach for solving both parts of the puzzle.

## Workflow for Solving

1. **Part 1**:
- Read the problem description in `part_1.txt`.
- Implement the solution in the `part_one` function within `main.py`.
- Run the script to verify the answer.

2. **Part 2**:
- *Note: Part 1 must be completed first as Part 2 often builds upon it.*
- *Note: Part 2 exists for most problems, but the last day usually has only one part.*
- Read the problem description in `part_2.txt`.
- Implement the solution in the `part_two` function within `main.py`.
- Run the script to verify the answer.

3. **Documentation**:
- Update the file `discussion.md` in the day's directory.
- Explain the logic and reasoning behind your solutions for both parts.

## Tips

The problem descriptions (`part_1.txt`, `part_2.txt`) will usually contain a sample data set as well as the expected answer for that sample dataset. Test your solution with this first to make sure you're on the right track, and then move onto the full dataset in `input.txt` (which could be hundreds or even thousands of lines long).

## Running the Solutions

You can run the solution for a specific day from the root directory of the project.

**Example for Day 1:**
```bash
python 2024/day_1/main.py
```

The script will automatically locate the `input.txt` file within the same directory and output the results for Part One and Part Two.
