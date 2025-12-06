import sys
import os

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.file_reader import read_input

def part_one(lines):
    disk_map = lines[0].strip()
    blocks = []
    file_id = 0

    for i, char in enumerate(disk_map):
        length = int(char)
        if i % 2 == 0:
            # File
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            # Free space
            blocks.extend([None] * length)

    # Compaction
    left = 0
    right = len(blocks) - 1

    while left < right:
        # Find leftmost free space
        while left < len(blocks) and blocks[left] is not None:
            left += 1

        # Find rightmost file block
        while right >= 0 and blocks[right] is None:
            right -= 1

        if left < right:
            blocks[left] = blocks[right]
            blocks[right] = None
            left += 1
            right -= 1

    # Checksum
    checksum = 0
    for i, block in enumerate(blocks):
        if block is not None:
            checksum += i * block

    return checksum

def part_two(lines):
    disk_map = lines[0].strip()
    segments = []
    file_id = 0

    for i, char in enumerate(disk_map):
        length = int(char)
        if length == 0:
            continue
        if i % 2 == 0:
            # File
            segments.append({'id': file_id, 'length': length, 'is_file': True})
            file_id += 1
        else:
            # Free space
            segments.append({'id': -1, 'length': length, 'is_file': False})

    max_file_id = file_id - 1

    for current_id in range(max_file_id, -1, -1):
        # Find the file segment
        file_index = -1
        for i, seg in enumerate(segments):
            if seg['is_file'] and seg['id'] == current_id:
                file_index = i
                break

        if file_index == -1:
            continue

        file_segment = segments[file_index]

        # Find leftmost free space that fits
        target_index = -1
        for i in range(file_index):
            seg = segments[i]
            if not seg['is_file'] and seg['length'] >= file_segment['length']:
                target_index = i
                break

        if target_index != -1:
            # Move the file
            target_segment = segments[target_index]
            remaining_space = target_segment['length'] - file_segment['length']

            # Replace target segment with file segment
            # We use a new dictionary to avoid reference issues
            segments[target_index] = {'id': file_segment['id'], 'length': file_segment['length'], 'is_file': True}

            # Insert remaining free space if any
            if remaining_space > 0:
                segments.insert(target_index + 1, {'id': -1, 'length': remaining_space, 'is_file': False})
                # Since we inserted, the old file_index increases by 1
                file_index += 1

            # Replace old file location with free space
            segments[file_index] = {'id': -1, 'length': file_segment['length'], 'is_file': False}

            # Merge free spaces at the old location
            # Check right neighbor first (to keep index stable)
            if file_index + 1 < len(segments) and not segments[file_index + 1]['is_file']:
                segments[file_index]['length'] += segments[file_index + 1]['length']
                segments.pop(file_index + 1)

            # Check left neighbor
            if file_index - 1 >= 0 and not segments[file_index - 1]['is_file']:
                segments[file_index - 1]['length'] += segments[file_index]['length']
                segments.pop(file_index)

    # Calculate checksum
    checksum = 0
    position = 0
    for seg in segments:
        if seg['is_file']:
            for i in range(seg['length']):
                checksum += (position + i) * seg['id']
        position += seg['length']

    return checksum

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input(input_path)

    print("Part One:", part_one(lines))
    print("Part Two:", part_two(lines))
