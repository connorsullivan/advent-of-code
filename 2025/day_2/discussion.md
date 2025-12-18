# Day 2

## Part One

The puzzle involves finding "invalid" product IDs where the ID is made of a sequence of digits repeated exactly twice (e.g., 55, 6464, 123123). Given ranges of IDs, we sum all invalid IDs.

The solution checks if a number's string representation has even length and if its first half equals its second half.

## Part Two

Part 2 extends the pattern to include sequences repeated at least twice. For example, 111 (1 three times), 565656 (56 three times), and 2121212121 (21 five times) are now invalid.

The solution tries all possible repeat lengths from 1 to half the string length and checks if the entire string is composed of that pattern repeated.
