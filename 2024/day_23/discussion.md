# Day 23

## Part One

**Problem:** Find all sets of three interconnected computers (triangles in the graph) where at least one computer's name starts with 't'.

**Approach:**
1. Parse the input to build an adjacency list representation of the network graph
2. For each node, examine all pairs of its neighbors
3. If two neighbors are also connected to each other, we have found a triangle
4. Store triangles as sorted tuples to avoid duplicates
5. Count triangles containing at least one node starting with 't'

**Key Insight:** A triangle exists when node A is connected to B and C, and B is also connected to C. By iterating through each node and checking all pairs of its neighbors, we can find all triangles efficiently.

**Answer:** 1194

## Part Two

**Problem:** Find the largest clique in the network (the maximum set of computers where every computer is connected to every other computer in the set).

**Approach:**
1. Build the same adjacency list graph representation
2. Use the Bron-Kerbosch algorithm to find all maximal cliques
3. The Bron-Kerbosch algorithm recursively explores candidate sets:
   - R: current clique being built
   - P: candidates that could extend the clique
   - X: already processed nodes (to avoid duplicates)
4. With pivot optimization, we reduce redundant recursive calls by choosing a pivot node with the most connections in P
5. Find the largest clique from all maximal cliques
6. Return the sorted, comma-separated list of computer names

**Key Insight:** The maximum clique problem is NP-complete, but the Bron-Kerbosch algorithm with pivot optimization is efficient for reasonably sized graphs. The pivot strategy minimizes branching by focusing on nodes less connected to the pivot.

**Answer:** bd,bu,dv,gl,qc,rn,so,tm,wf,yl,ys,ze,zr
