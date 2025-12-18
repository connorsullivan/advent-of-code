# Day 1

## Part One
Track the dial position modulo 100 starting at 50. After each rotation, update the position with a signed offset and count how many rotations end with the dial at 0.

## Part Two
For each rotation, count every click that lands on 0. The first time 0 is hit occurs after `position` left clicks or `100-position` right clicks (treating 0 as 100). If the rotation length exceeds that point, additional hits occur every 100 clicks. Sum these hits while updating the dial position as in part one.
