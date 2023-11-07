# The mode of a group of numbers is the value (or values) that occur most often (values have to occur more than once). Given a sorted 
# list of numbers, return a list of all modes in ascending order.

# Examples

# mode([4, 5, 6, 6, 6, 7, 7, 9, 10]) ➞ [6] 

# mode([4, 5, 5, 6, 7, 8, 8, 9, 9]) ➞ [5, 8, 9]

# mode([1, 2, 2, 3, 6, 6, 7, 9]) ➞ [2, 6] 

def mode(nums):
	return sorted(list(set(filter(lambda x: nums.count(x)==max(map(lambda x: nums.count(x),nums)),nums))))

print(mode([4, 5, 6, 6, 6, 7, 7, 9, 10])) # ➞ [6] 
print(mode([4, 5, 5, 6, 7, 8, 8, 9, 9])) # ➞ [5, 8, 9]
print(mode([1, 2, 2, 3, 6, 6, 7, 9])) # ➞ [2, 6] 

# from collections import Counter

# def mode(nums):
# 	c = Counter(nums)
# 	return [x for x,y in sorted(c.items()) if y == max(c.values())]

# def mode(nums):
# 	m = max(nums.count(i) for i in nums)
# 	return [i for i in sorted(set(nums)) if nums.count(i)==m]

# mode=lambda n:sorted(i for i in set(n) if n.count(i)==max(map(n.count,n)))