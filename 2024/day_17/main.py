import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

class Computer:
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.ip = 0
        self.output = []

    def get_combo_value(self, operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        else:
            raise ValueError("Invalid combo operand 7")

    def run(self):
        while self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]

            if opcode == 0: # adv
                denom = 2 ** self.get_combo_value(operand)
                self.a = self.a // denom
                self.ip += 2
            elif opcode == 1: # bxl
                self.b = self.b ^ operand
                self.ip += 2
            elif opcode == 2: # bst
                self.b = self.get_combo_value(operand) % 8
                self.ip += 2
            elif opcode == 3: # jnz
                if self.a != 0:
                    self.ip = operand
                else:
                    self.ip += 2
            elif opcode == 4: # bxc
                self.b = self.b ^ self.c
                self.ip += 2
            elif opcode == 5: # out
                val = self.get_combo_value(operand) % 8
                self.output.append(val)
                self.ip += 2
            elif opcode == 6: # bdv
                denom = 2 ** self.get_combo_value(operand)
                self.b = self.a // denom
                self.ip += 2
            elif opcode == 7: # cdv
                denom = 2 ** self.get_combo_value(operand)
                self.c = self.a // denom
                self.ip += 2

        return ",".join(map(str, self.output))

def parse_input(lines):
    a = int(lines[0].split(": ")[1])
    b = int(lines[1].split(": ")[1])
    c = int(lines[2].split(": ")[1])
    # lines[3] is empty usually, but let's find the line starting with Program
    program_line = next(line for line in lines if line.startswith("Program:"))
    program = list(map(int, program_line.split(": ")[1].split(",")))
    return a, b, c, program

def part_one(lines):
    a, b, c, program = parse_input(lines)
    computer = Computer(a, b, c, program)
    return computer.run()

def run_program(a, b, c, program):
    computer = Computer(a, b, c, program)
    output_str = computer.run()
    if not output_str:
        return []
    return list(map(int, output_str.split(",")))

def part_two(lines):
    _, b_init, c_init, program = parse_input(lines)

    # We want to find A such that output == program
    # We build A from 0, 3 bits at a time, matching the program from end to start.

    candidates = [0]

    for i in range(len(program)):
        next_candidates = []
        expected_suffix = program[-(i+1):]

        for val in candidates:
            for k in range(8):
                new_val = val * 8 + k

                output = run_program(new_val, b_init, c_init, program)

                if output == expected_suffix:
                    next_candidates.append(new_val)

        candidates = next_candidates

    if candidates:
        return min(candidates)
    return None

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
