# Write a function that returns the total number of integers covered from a list of intervals (inclusive). In other words, return 
# the number of different integers in the lists.

# Examples

# covered_integers([[80, 81], [1, 2], [9, 11]]) ➞ 7
# # Seven integers are covered: 1, 2, 9, 10, 11, 80, 81

# covered_integers([[3, 6], [4, 6], [5, 6]]) ➞ 4

# covered_integers([[1, 2], [1, 2]]) ➞ 2

# Notes

#     Intervals may overlap, be subintervals of each other, or be identical.
#     For each interval [l, u], l and u will be integers, and l <= u will always be true.

def covered_integers(lst):
	ints = sorted(list(set(y for x in lst if x[0] != x[1] for y in x)))
	dupes = len([1 for x in lst if x[0]==x[1] and x[0] not in ints])
	return sum([ints[i+1]-ints[i]+1 for i in range(0,len(ints)-1,2)]) + dupes

# write out list of steps to factor the above code.

# print(covered_integers([[80, 81], [1, 2], [9, 11]])) # ➞ 7
# # Seven integers are covered: 1, 2, 9, 10, 11, 80, 81
# print(covered_integers([[3, 6], [4, 6], [5, 6]])) # ➞ 4
# print(covered_integers([[1, 2], [1, 2]])) # ➞ 2

print(covered_integers([[80, 81], [1, 2], [9, 11]])) #, 7)
print(covered_integers([[3, 6], [4, 6], [5, 6]])) #, 4)
print(covered_integers([[1, 2], [1, 2]])) #, 2)
print(covered_integers([[1, 11]])) #, 11)
print(covered_integers([[8, 9], [102, 104]])) #, 5)
print(covered_integers([[1, 1], [5, 5], [8, 8]])) #, 3)
print(covered_integers([[0, 5], [5, 5], [8, 8]])) #, 7)
print(covered_integers([[1, 5], [3, 5], [4, 6], [5, 7]])) #, 7)
print(covered_integers([[-3, 10], [-2, 9], [-1, 8], [0, 7], [1, 6], [2, 5], [3, 4]])) #, 14)

# def covered_integers(lst):
# 	return len(set([j for i in lst for j in range(i[0],i[1]+1)]))

# def covered_integers(lst):
# 	return len({i for l, u in lst for i in range(l, u+1)})