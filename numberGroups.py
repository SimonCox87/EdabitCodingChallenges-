# Given three groups of numbers, return a list containing all numbers that appear in more than one group (in ascending 
# order).
# Examples

# number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]) ➞ []

# number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]) ➞ [1, 3]

# number_groups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2]) ➞ [2, 4, 9]

# number_groups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6]) ➞ [5, 8]

def number_groups(group1, group2, group3):
    a,b,c = set(group1),set(group2),set(group3)
    return sorted(set(j for i in (a & b, a & c, b & c) for j in i))

# print(number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5])) # ➞ []
# print(number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3])) # ➞ [1, 3]
# print(number_groups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2])) # ➞ [2, 4, 9]
# print(number_groups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6])) # ➞ [5, 8]

print(number_groups([3, 1, 7, 6, 4], [6, 10, 2, 2, 6], [1, 1, 2, 5, 5])) #, [1, 2, 6])
print(number_groups([6, 3, 7, 3, 1], [4, 6, 5, 9, 2], [10, 7, 8, 1, 2])) #, [1, 2, 6, 7])
print(number_groups([4, 6, 3, 9, 9], [4, 7, 10, 6, 9], [7, 9, 1, 1, 5])) #, [4, 6, 7, 9])
print(number_groups([7, 6, 9, 2, 6], [8, 5, 6, 8, 3], [5, 8, 6, 8, 3])) #, [3, 5, 6, 8])
print(number_groups([4, 4, 4, 5, 1], [8, 2, 8, 9, 4], [7, 4, 3, 10, 4])) #, [4])
print(number_groups([4, 8, 9, 8, 4], [10, 2, 5, 7, 2], [1, 1, 3, 6, 6])) #, [])
print(number_groups([7, 10, 7, 1, 4], [6, 2, 1, 8, 5], [9, 4, 9, 9, 3])) #, [1, 4])
print(number_groups([4, 3, 3, 5, 9], [6, 9, 6, 6, 1], [10, 5, 7, 10, 7])) #, [5, 9])
print(number_groups([3, 4, 9, 1, 10], [2, 9, 6, 8, 5], [6, 9, 10, 1, 7])) #, [1, 6, 9, 10])
print(number_groups([4, 7, 2, 5, 9], [6, 10, 2, 2, 10], [9, 9, 2, 9, 9])) #, [2, 9])
print(number_groups([7, 10, 4, 8, 2], [3, 8, 1, 9, 4], [6, 1, 5, 8, 6])) #, [1, 4, 8])
print(number_groups([10, 1, 10, 10, 3], [7, 6, 8, 7, 4], [7, 7, 7, 2, 10])) #, [7, 10])
print(number_groups([7, 7, 6, 8, 3], [3, 3, 10, 3, 10], [5, 7, 2, 2, 10])) #, [3, 7, 10])
print(number_groups([5, 9, 9, 9, 5], [8, 6, 1, 1, 1], [3, 7, 2, 2, 6])) #, [6])
print(number_groups([2, 8, 10, 2, 10], [8, 9, 4, 6, 8], [6, 5, 4, 1, 10])) #, [4, 6, 8, 10])
print(number_groups([1, 5, 3, 3, 5], [9, 5, 10, 8, 10], [4, 6, 1, 6, 10])) #, [1, 5, 10])
print(number_groups([2, 6, 5, 4, 4], [8, 4, 8, 7, 8], [6, 8, 8, 3, 5])) #, [4, 5, 6, 8])
print(number_groups([8, 8, 9, 3, 8], [5, 1, 10, 6, 1], [2, 7, 7, 4, 2])) #, [])
print(number_groups([1, 10, 6, 10, 3], [9, 3, 9, 6, 8], [7, 8, 5, 3, 6])) #, [3, 6, 8])
print(number_groups([9, 8, 2, 9, 1], [10, 3, 2, 5, 6], [1, 7, 8, 3, 7])) #, [1, 2, 3, 8])

# def number_groups(*g):
# 	a, b, c = [set(i) for i in g]
# 	return sorted(set.union(a.intersection(b),a.intersection(c),b.intersection(c)))

# def number_groups(*L):
# 	A, B, C = map(set, L)
# 	return sorted(A & B | B & C | C & A)

# def number_groups(g1, g2, g3):
# 	return [n for n in set(g1+g2+g3) if sum(n in g for g in [g1,g2,g3])>1]