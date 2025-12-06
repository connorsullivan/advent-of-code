# Day 2: Red-Nosed Reports

## Part 1

The problem asks us to identify "safe" reports. A report is a sequence of numbers (levels). A report is safe if:
1.  The levels are either all increasing or all decreasing.
2.  Any two adjacent levels differ by at least 1 and at most 3.

### Approach
I implemented a helper function `is_safe(report)` that:
1.  Calculates the differences between adjacent levels.
2.  Checks if all differences are between 1 and 3 (increasing).
3.  Checks if all differences are between -3 and -1 (decreasing).
4.  Returns `True` if either condition is met.

I iterated through each line of the input, parsed the numbers, and used `is_safe` to count the valid reports.

### Complexity
-   **Time Complexity**: $O(N \times M)$, where $N$ is the number of reports and $M$ is the average length of a report. Since $M$ is small, this is effectively linear with respect to the input size.
-   **Space Complexity**: $O(M)$ to store the report and differences.

## Part 2

The "Problem Dampener" allows us to remove a single level from an unsafe report to make it safe.

### Approach
For each report:
1.  Check if it is safe using the Part 1 logic.
2.  If it is not safe, iterate through each index of the report.
3.  Create a new report with the element at the current index removed.
4.  Check if this modified report is safe.
5.  If any modified report is safe, count the original report as safe.

### Complexity
-   **Time Complexity**: $O(N \times M^2)$. For each unsafe report, we might check up to $M$ modified versions, each taking $O(M)$ time to verify. Given the small constraints on $M$, this is still very efficient.
-   **Space Complexity**: $O(M)$ to store the modified reports.
