# Day 7

## Part One

The problem involves simulating tachyon beam propagation through a manifold. Beams start at 'S' and move downward. When a beam hits a splitter ('^'), it stops and creates two new beams: one to the left and one to the right. Beams at the same position merge. We need to count the total number of split events.

The solution:
1. Find the starting position 'S'
2. Use a set to track beam positions to handle merging automatically
3. Simulate step-by-step: for each beam, move it down one row
4. If a beam hits a splitter, increment the split counter and create two new beams (left and right)
5. Continue until all beams exit the manifold

Time complexity: O(rows × unique_positions) where unique_positions is bounded by the number of columns.

## Part Two

Part two introduces quantum mechanics: a single particle takes ALL possible paths simultaneously, creating separate timelines at each splitter. We need to count the total number of unique timelines (paths), not just unique endpoints.

The solution:
1. Use recursive DFS with memoization to count paths
2. From each position, if we hit a splitter, the number of paths is the sum of paths from the left branch and the right branch
3. If we exit the manifold, that counts as 1 path
4. Memoization is crucial to avoid recalculating paths from the same position

The key insight is that this is counting paths in a DAG (directed acyclic graph), not counting unique endpoints. Multiple paths can end at the same location.

Time complexity: O(rows × cols) with memoization, as each position is visited at most once.
