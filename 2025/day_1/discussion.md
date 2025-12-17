# Day 1

## Part One
The problem asks us to track the position of a dial (0-99) starting at 50. We process a series of rotations (Left or Right) and count how many times the dial ends up at 0 after a rotation.
The dial is circular, so we use modulo 100 for all calculations. For left rotations, we subtract the distance and take modulo 100. For right rotations, we add the distance and take modulo 100.

## Part Two
In Part Two, we need to count how many times the dial points at 0 *during* or *after* each rotation.
For a right rotation of distance $d$ starting at position $p$:
The dial hits 0 if $p + i \equiv 0 \pmod{100}$ for $1 \le i \le d$.
This is equivalent to counting integers $k$ such that $p + 1 \le 100k \le p + d$.
The number of such $k$ is $\lfloor (p + d) / 100 \rfloor - \lfloor p / 100 \rfloor$.

For a left rotation of distance $d$ starting at position $p$:
The dial hits 0 if $p - i \equiv 0 \pmod{100}$ for $1 \le i \le d$.
This is equivalent to counting integers $k$ such that $p - d \le 100k \le p - 1$.
The number of such $k$ is $\lfloor (p - 1) / 100 \rfloor - \lfloor (p - d - 1) / 100 \rfloor$.

Summing these counts over all rotations gives the final answer.
