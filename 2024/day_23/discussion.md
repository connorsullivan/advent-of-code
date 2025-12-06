# Day 23: LAN Party

## Part 1
The problem asks us to find sets of 3 inter-connected computers (triangles in the graph) where at least one computer's name starts with 't'.

### Approach
1.  **Parse the Input**: Build an adjacency list representing the network. The graph is undirected.
2.  **Find Triangles**: Iterate through all nodes `u`. For each neighbor `v` of `u` (where `v > u` to avoid duplicates), find the intersection of neighbors of `u` and neighbors of `v`. Any node `w` in this intersection forms a triangle `{u, v, w}`.
3.  **Filter**: Check if any node in the triangle starts with 't'.
4.  **Count**: Return the number of valid triangles.

### Complexity
-   **Time**: $O(V \cdot d^2)$ or $O(E \cdot d)$, where $V$ is the number of vertices, $E$ is the number of edges, and $d$ is the maximum degree. In the worst case (dense graph), it's $O(V^3)$. Given the input size, this is efficient enough.
-   **Space**: $O(V + E)$ to store the graph.

## Part 2
The problem asks for the password to the LAN party, which corresponds to the largest set of fully connected computers (the maximum clique).

### Approach
1.  **Maximum Clique**: Use the **Bron-Kerbosch algorithm** with pivoting and pruning to find the maximum clique in the graph.
    -   **Pivoting**: Choose a pivot vertex to minimize the number of recursive branches.
    -   **Pruning**: If the size of the current clique plus the number of candidate vertices is not greater than the size of the largest clique found so far, backtrack immediately.
2.  **Format Output**: Sort the names of the computers in the maximum clique alphabetically and join them with commas.

### Complexity
-   **Time**: The Maximum Clique problem is NP-hard. However, the Bron-Kerbosch algorithm is very efficient for sparse graphs and typical inputs. The worst-case time complexity is $O(3^{V/3})$, but with pivoting and pruning, it runs much faster in practice.
-   **Space**: $O(V + E)$ for the graph and recursion stack.
