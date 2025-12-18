# Day 1

## Part One

Simulate the dial as a position `0..99`, starting at `50`.
Each instruction updates the position with modular arithmetic:

- `Rk`: `pos = (pos + k) % 100`
- `Lk`: `pos = (pos - k) % 100`

Count how many rotations end with `pos == 0`.

## Part Two

Instead of only checking the end position, count every click during each rotation.
For a rotation with distance `d`, the dial visits positions:

`pos + sign*1, pos + sign*2, ..., pos + sign*d (mod 100)`

So we just need to count how many `k` in `1..d` solve:

`(pos + sign*k) % 100 == 0`

This is one congruence class modulo `100`, so the count is:

- find the first `k0` in `1..100` that lands on `0`
- answer is `0` if `k0 > d`, else `1 + (d - k0) // 100`

Then update `pos` exactly as in part one.
