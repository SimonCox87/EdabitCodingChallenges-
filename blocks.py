"""A block sequence in three dimensions. We can write a formula for this one:

1 -> 5, 2-> 12, 3 -> 20, 4 -> 29, 5 -> 39

Sequence Step 1 - 5

Create a function that takes a number (step) as an argument and returns the amount of blocks in that step.
Examples

blocks(1) ➞ 5

blocks(5) ➞ 39

blocks(2) ➞ 12

Notes

    Step 0 obviously has to return 0.
    The input is always a positive integer."""

def blocks(step):
    return 0 if not step else (0.5 * step **2) + (5.5 * step) - 1

print(blocks(0))
print(blocks(1))
print(blocks(2))
print(blocks(3))
print(blocks(4))
print(blocks(5))
