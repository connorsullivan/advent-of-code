# Day 9: Disk Fragmenter

## Problem Summary
This problem involves compacting a disk by moving file blocks around to eliminate gaps. The input is a dense disk map where digits alternate between file lengths and free space lengths.

## Part One: Block-by-Block Compaction

### Approach
1. Parse the disk map into individual blocks (files have IDs, free space is represented as None)
2. Use a two-pointer approach: left pointer finds free space, right pointer finds file blocks
3. Move blocks one at a time from the end to the leftmost free space
4. Calculate checksum by summing (position × file_id) for all file blocks

### Key Insight
The two-pointer technique efficiently compacts the disk in O(n) time by simultaneously scanning from both ends.

**Result: 6279058075753**

## Part Two: Whole File Compaction

### Approach
1. Parse the disk map and track each file's position and length
2. Process files in decreasing file ID order (highest ID first)
3. For each file, search for the leftmost contiguous free space that can fit it (only looking to the left of the file's current position)
4. If found, move the entire file to that location
5. Calculate checksum the same way as Part 1

### Key Insight
Unlike Part 1, we must:
- Keep files together (move all blocks of a file at once)
- Only search for free space to the left of the file
- Process in reverse file ID order
- Files that can't fit in any free space to their left stay in place

The algorithm preserves the integrity of each file while still maximizing contiguous free space.

**Result: 6301361958738**

## Implementation Details

Both solutions represent the disk as a list where:
- File blocks contain their file ID (integer)
- Free space blocks contain None

This representation makes it easy to manipulate blocks and calculate the checksum. The main difference is that Part 1 moves individual blocks while Part 2 moves entire files as units.
