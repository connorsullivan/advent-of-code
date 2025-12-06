# Day 9 Solutions

## Part 1

The goal is to compact the disk by moving individual file blocks from the end to the leftmost free space.

### Approach

1.  **Parse Input**: Convert the dense disk map string into a list of blocks. Each block is either a file ID (integer) or `None` (free space).
2.  **Two-Pointer Compaction**: Use a `left` pointer starting at the beginning and a `right` pointer starting at the end.
    - Advance `left` until it finds a free space.
    - Retreat `right` until it finds a file block.
    - If `left < right`, swap the blocks.
3.  **Checksum**: Iterate through the compacted list and sum `index * file_id` for all file blocks.

**Complexity**:
-   **Time**: $O(N)$, where $N$ is the total number of blocks. We traverse the list once.
-   **Space**: $O(N)$ to store the expanded list of blocks.

## Part 2

The goal is to compact the disk by moving **whole files** to the leftmost sufficient free space, processing files in decreasing order of ID.

### Approach

1.  **Parse Input**: Convert the disk map into a list of `Segment` objects (dictionaries), where each segment has an ID, length, and type (file or free).
2.  **Process Files**: Iterate through file IDs from the maximum ID down to 0.
    - Locate the segment corresponding to the current file ID.
    - Scan the segments from the left to find the first free space segment with `length >= file_length`.
    - If a suitable free space is found:
        - Move the file to that location.
        - If the free space was larger than the file, split it into the file and the remaining free space.
        - Replace the file's old location with free space.
        - **Merge** the new free space at the old location with its neighbors if they are also free space, to maintain contiguous free space segments.
3.  **Checksum**: Iterate through the final segments, calculating the position of each block and adding to the checksum.

**Complexity**:
-   **Time**: $O(F \times S)$, where $F$ is the number of files and $S$ is the number of segments. Since $F$ and $S$ are proportional to the input string length, this is roughly quadratic with respect to the input size. With ~10k files, this is efficient enough.
-   **Space**: $O(S)$ to store the list of segments.
