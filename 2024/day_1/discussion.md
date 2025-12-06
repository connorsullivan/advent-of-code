# Day 1 Solutions

## Part 1

### Approach
The problem asks us to calculate the total distance between two lists of numbers. The distance is defined as the sum of the absolute differences between the sorted pairs of numbers from both lists.

1.  **Parsing**: Read the input file line by line. Split each line into two numbers and append them to `left_list` and `right_list` respectively.
2.  **Sorting**: Sort both `left_list` and `right_list` in ascending order. This ensures we are pairing the smallest with the smallest, second smallest with second smallest, etc.
3.  **Calculation**: Iterate through the sorted lists simultaneously. For each pair `(left, right)`, calculate `abs(left - right)` and add it to the `total_distance`.

### Complexity
-   **Time Complexity**: $O(N \log N)$, where $N$ is the number of lines in the input. This is dominated by the sorting step.
-   **Space Complexity**: $O(N)$ to store the two lists.

## Part 2

### Approach
The second part asks for a "similarity score". This is calculated by summing each number in the left list multiplied by the number of times it appears in the right list.

1.  **Parsing**: Same as Part 1.
2.  **Frequency Map**: Create a frequency map (or hash map) of the numbers in `right_list`. In Python, `collections.Counter` is perfect for this. It maps each number to its count.
3.  **Calculation**: Iterate through each number in `left_list`. Look up its count in the frequency map (defaulting to 0 if not found). Add `number * count` to the `similarity_score`.

### Complexity
-   **Time Complexity**: $O(N)$. Creating the Counter takes $O(N)$, and iterating through the left list takes $O(N)$. Lookups in the Counter are $O(1)$ on average.
-   **Space Complexity**: $O(N)$ to store the lists and the frequency map.
