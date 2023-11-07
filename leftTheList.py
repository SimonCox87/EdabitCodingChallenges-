# You are given two lists. The elements in lst1 threw a party and started to mix around. However, one of the elements got lost! Your 
# task is to return the element which was lost.

# Examples

# missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]) ➞ 2

# missing([True, True, False, False, True], [False, True, False, True]) ➞ True

# missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]) ➞ "ugly"

# missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]) ➞ (5,)

# Notes

#     Assume that the first list always contains 1 or more elements.
#     Elements are always lost.
#     An element can also have duplicates.

def missing(lst1, lst2):
    return[i for i in lst1 if lst1.count(i)!=lst2.count(i)][0]

print(missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8])) # ➞ 2
print(missing([True, True, False, False, True], [False, True, False, True])) # ➞ True
print(missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"])) # ➞ "ugly"
print(missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5])) # ➞ (5,)

"""def missing(a, b):
	for i in b:
		a.remove(i)
	return a[0]"""