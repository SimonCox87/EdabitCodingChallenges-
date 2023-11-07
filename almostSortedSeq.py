# An almost-sorted sequence is a sequence that is strictly increasing or strictly decreasing if you remove a single element 
# from the list (no more, no less). Write a function that returns True if a list is almost-sorted, and False otherwise.

# For example, if you remove 80 from the first example, it is perfectly sorted in ascending order. Similarly, if you remove 7 
# from the second example, it is perfectly sorted in descending order.

# Examples

# almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ) ➞ True

# almost_sorted([6, 5, 4, 7, 3]) ➞ True

# almost_sorted([6, 4, 2, 0]) ➞ False
# // Sequence is already sorted.

# almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) ➞ False
# // Requires removal of more than 1 item.

# Notes

#     Completely sorted lists should return False.
#     Lists will always be > 3 in length (to remove ambiguity).
#     Numbers in each input list will be unique - don't worry about "ties".

def almost_sorted(lst):
    l = [lst[i] for i in range(1,len(lst)-1) if lst[i]>lst[i+1] and lst[i]>lst[i-1] or lst[i]<lst[i+1] and lst[i]<lst[i-1]]
    return len(l) == 1 or len(l) == 2

# print(almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41])) # ➞ True
# print(almost_sorted([6, 5, 4, 7, 3])) # ➞ True
# print(almost_sorted([6, 4, 2, 0])) # ➞ False
# # // Sequence is already sorted.
# print(almost_sorted([7, 8, 9, 3, 10, 11, 12, 2])) # ➞ False
# # // Requires removal of more than 1 item.

print(almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41])) #, True, 'remove 80 should work')
print(almost_sorted([6, 5, 4, 7, 3])) #, True, 'remove 7 should work')
print(almost_sorted([6, 4, 2, 0])) #, False, 'numbers should not be completely sorted')
print(almost_sorted([7, 8, 9, 3, 10, 11, 12, 2])) #, False)
print(almost_sorted([9, 1, 8, 2])) #, True, 'remove 1 should work')
print(almost_sorted([1, 3, 9, 44, 15, 17, 33])) #, True, 'remove 44 should work')
print(almost_sorted([5, 4, 3, 2, -1, 0])) #, True, 'remove -1 should work')
print(almost_sorted([5, 2, 3, 4])) #, True, 'remove 5 should work')
print(almost_sorted([8, 3, 7, 4, 9])) #, False)
print(almost_sorted([-3, -4, -5, -7])) #, False, 'numbers should not be completely sorted')
print(almost_sorted([5, 6, 7, 8])) #, False, 'numbers should not be completed sorted')
print(almost_sorted([9, 1, 8, 2, 7, 3])) #, False)

# def almost_sorted(lst):
# 	score = sum(a < b for a, b in zip(lst, lst[1:]))
# 	return score in [1, len(lst) - 2]

# def almost_sorted(lst):
# 	a = [i>j for i,j in zip(lst,lst[1:])].count(True)
# 	return a==1 or len(lst)-a==2

# def almost_sorted(lst):
# 	s = sum(lst[x] > lst[x-1] for x in range(1,len(lst))) 
# 	return s == len(lst) - 2 or s == 1

# In future use he zip function to compare adjacent elements in a list.  Shorter solution.