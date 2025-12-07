import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    disk_map = lines[0].strip()

    # Parse the disk map into blocks
    blocks = []
    file_id = 0
    for i, length in enumerate(disk_map):
        length = int(length)
        if i % 2 == 0:  # File
            blocks.extend([file_id] * length)
            file_id += 1
        else:  # Free space
            blocks.extend([None] * length)

    # Compact by moving blocks from end to leftmost free space
    left = 0
    right = len(blocks) - 1

    while left < right:
        # Find next free space from left
        while left < right and blocks[left] is not None:
            left += 1

        # Find next file block from right
        while left < right and blocks[right] is None:
            right -= 1

        # Move block
        if left < right:
            blocks[left] = blocks[right]
            blocks[right] = None

    # Calculate checksum
    checksum = 0
    for pos, file_id in enumerate(blocks):
        if file_id is not None:
            checksum += pos * file_id

    return checksum

def part_two(lines):
    disk_map = lines[0].strip()

    # Parse the disk map into blocks
    blocks = []
    file_id = 0
    file_info = {}  # file_id -> (start_pos, length)

    pos = 0
    for i, length in enumerate(disk_map):
        length = int(length)
        if i % 2 == 0:  # File
            file_info[file_id] = (pos, length)
            blocks.extend([file_id] * length)
            file_id += 1
            pos += length
        else:  # Free space
            blocks.extend([None] * length)
            pos += length

    # Move files in decreasing file ID order
    max_file_id = file_id - 1
    for fid in range(max_file_id, -1, -1):
        start_pos, file_length = file_info[fid]

        # Find leftmost span of free space that can fit this file
        free_start = None
        free_length = 0

        for i in range(start_pos):  # Only look to the left
            if blocks[i] is None:
                if free_start is None:
                    free_start = i
                free_length += 1

                if free_length >= file_length:
                    # Found a suitable spot, move the file
                    # Clear old position
                    for j in range(start_pos, start_pos + file_length):
                        blocks[j] = None

                    # Place in new position
                    for j in range(free_start, free_start + file_length):
                        blocks[j] = fid

                    # Update file_info for this file
                    file_info[fid] = (free_start, file_length)
                    break
            else:
                # Reset free space search
                free_start = None
                free_length = 0

    # Calculate checksum
    checksum = 0
    for pos, file_id in enumerate(blocks):
        if file_id is not None:
            checksum += pos * file_id

    return checksum

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
