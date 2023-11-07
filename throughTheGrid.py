# How many ways are there to navigate through a grid (w * h)?

# https://edabit.com/challenge/LSpPdiycJ75MiwvgQ

# Grid

# Suppose you're on a 4 × 6 grid, and want to go from the bottom left to the top right. How many different paths can you 
# take? Avoid backtracking, you can only move right or up.

# Create a function that takes width and height and returns the amount of possibilities.
# Examples

# grid_pos([1, 1]) ➞ 2

# grid_pos([6, 4]) ➞ 210

# grid_pos([5, 5]) ➞ 252

def fac(n):
    return n*fac(n-1) if n!=1 else 1
def grid_pos(lst):
    return fac(sum(lst)) // (fac(lst[0])*fac(lst[1]))

print(grid_pos([1, 1])) # ➞ 2
print(grid_pos([6, 4])) # ➞ 210
print(grid_pos([5, 5])) # ➞ 252

# def grid_pos(lst):
#     def factorial(x):
#         if x<=1:
#             return 1
#         return x*factorial(x-1)
#     return factorial(sum(lst))/factorial(lst[0])/factorial(lst[1])