"""There are three cups on a table, at positions A, B, and C. At the start, there is a ball hidden under the cup at position B.

Image of cups where ball is under middle cup

However, I perform several swaps on the cups, which is notated as two letters. For example, if I swap the cups at positions A and 
B, I could notate this as AB or BA.

Create a function that returns the letter position that the ball is at, once I finish swapping the cups. The swaps will be given 
to you as a list.
Worked Example

cup_swapping(["AB", "CA", "AB"]) ➞ "C"

# Ball begins at position B.
# Cups A and B swap, so the ball is at position A.
# Cups C and A swap, so the ball is at position C.
# Cups A and B swap, but the ball is at position C, so it doesn't move.

Examples

cup_swapping(["AB", "CA"]) ➞ "C"

cup_swapping(["AC", "CA", "CA", "AC"]) ➞ "B"

cup_swapping(["BA", "AC", "CA", "BC"]) ➞ "A"

Notes

    A swap could be notated in two different ways, since both ways end up with the same outcome.
    All swaps will be notated as capital letters and will be valid.
    You cannot swap a cup with itself."""

def cup_swapping(swaps):
    ballPosition = "B"
    for swap in swaps:
        if ballPosition in swap:
            if ballPosition == swap[0]:
                ballPosition = swap[1]
            else:
                ballPosition = swap[0]
    return ballPosition

"""print(cup_swapping(["AB", "CA"]))
print(cup_swapping(["AC", "CA", "CA", "AC"]))
print(cup_swapping(["BA", "AC", "CA", "BC"]))"""

print(cup_swapping(['AB', 'CA'])) #C
print(cup_swapping(['AB', 'CA', 'AB'])) #C
print(cup_swapping(['AC', 'CA', 'CA', 'AC'])) #B
print(cup_swapping(['BA', 'AC', 'CA', 'BC'])) #A
print(cup_swapping(['BC', 'CB', 'CA', 'BA'])) #A
print(cup_swapping(['BC'])) #C
print(cup_swapping(['BA', 'CA', 'CB', 'CA'])) #B
print(cup_swapping([])) #B

"""def cup_swapping(swaps):
    ball = "B"
    for move in swaps:
        if ball in move:
            ball = move[1] if move[0] == ball else move[0]
    return ball"""

