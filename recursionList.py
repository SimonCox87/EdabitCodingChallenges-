# Create a function that sums up all the elements in the list recursively. The use of the sum() built-in function is not allowed, 
# thus, the approach is recursive.

# Examples

# recur_add([1, 2, 3, 4, 10, 11]) ➞ 31

# recur_add([-3, 4, 11, 10, 21, 32, -9]) ➞ 66

# recur_add([-21, -7, 19, 3, 4, -8]) ➞ -10

def recur_add(lst):
    return lst.pop() + recur_add(lst) if lst else 0

print(recur_add([1, 2, 3, 4, 10, 11])) # ➞ 31
print(recur_add([-3, 4, 11, 10, 21, 32, -9])) # ➞ 66
print(recur_add([-21, -7, 19, 3, 4, -8])) # ➞ -10

# def recur_add(lst):
#     return 0 if not lst else lst[0] + recur_add(lst[1:])