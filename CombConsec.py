"""Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
Examples

consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True

Notes

    The input lists will have unique values."""

def consecutive_combo(lst1, lst2):
    lst = sorted(lst1 + lst2)
    consec = True

    for i in range(len(lst) - 1):
        if lst[i] + 1 == lst[i + 1]:
            consec = True
        else:
            consec = False
            break
    return consec

print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
print(consecutive_combo([44, 46], [45]))

"""def consecutive_combo(lst1, lst2):
	lst3 = lst1 + lst2
	return max(lst3) - min(lst3) == len(lst3) - 1"""

"""def consecutive_combo(lst1, lst2):
  lst = sorted(lst1+lst2)
  return all(lst[i]-lst[i-1]==1 for i in range(1,len(lst)))"""

"""cutive_combo(lst1, lst2):
	return sorted(lst1 + lst2) == list(range(min(lst1 + lst2), max(lst1 + lst2)+1))"""