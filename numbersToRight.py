# Create a function that retrieves every number that is strictly larger than every number that follows it.
# Examples

# larger_than_right([3, 13, 11, 2, 1, 9, 5]) ➞ [13, 11, 9, 5]
# # 13 is larger than all numbers to its right, etc.

# larger_than_right([5, 5, 5, 5, 5, 5]) ➞ [5]
# # Must be strictly larger.
# # Always include the last number.

# larger_than_right([5, 9, 8, 7]) ➞ [9, 8, 7]

# Notes

# The last number in an array is trivially strictly larger than all numbers that follow it (no numbers follow it).

def larger_than_right(lst):
    return[lst[i] for i in range(len(lst)-1) if lst[i]==max(lst[i:]) and lst[i]!=lst[i+1]]+[lst[-1]]

# print(larger_than_right([3, 13, 11, 2, 1, 9, 5]))
# print(larger_than_right([5, 5, 5, 5, 5, 5]))
# print(larger_than_right([5, 9, 8, 7]))

print(larger_than_right([3, 13, 11, 2, 1, 9, 5])) #, [13, 11, 9, 5])
print(larger_than_right([9, 8, 7, 6])) #, [9, 8, 7, 6])
print(larger_than_right([1, 2, 3, 4])) #, [4])
print(larger_than_right([5, 9, 8, 7])) #, [9, 8, 7])
print(larger_than_right([5, 5, 5, 5, 5])) #,[5])

"""def larger_than_right(lst):
	return [lst[i] for i in range(len(lst)) if lst[i] > max(lst[i+1:] + [0])]"""

"""def larger_than_right(l):
    return [a for i, a in enumerate(l) if a > max(l[i+1:] or [0])]"""

