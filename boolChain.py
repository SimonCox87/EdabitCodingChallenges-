"""Write three functions:

    boolean_and
    boolean_or
    boolean_xor

These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating pairwise.
Examples

boolean_and([True, True, False, True]) ➞ False
# [True, True, False, True] => [True, False, True] => [False, True] => False

boolean_or([True, True, False, False]) ➞ True
# [True, True, False, True] => [True, False, False] => [True, False] => True

boolean_xor([True, True, False, False]) ➞ False
# [True, True, False, False] => [False, False, False] => [False, False] => False

Notes

    XOR is the same as OR, except that it excludes [True, True].
    Each time you evaluate an element at 0 and at 1, you collapse it into the single result."""

def boolean_and(lst):
    return all(True if lst[i] == True and lst[i+1] ==True else False for i in range(len(lst) - 1))
	

def boolean_or(lst):
    return any(True if lst[i] == True or lst[i+1] == True else False for i in range(len(lst) -1))
	
def boolean_xor(lst):
    for i in range(len(lst) - 1):
        if lst[i] == lst[i+1]:
            lst[i+1] = False
        else:
            lst[i+1] = True

    return lst[-1]

#print(boolean_and([True, True, False, True]))
#print(boolean_or([True, True, False, False]))
#print(boolean_xor([True, True, False, False]))

# AND tests
"""print(boolean_and([True, True, False, True]))
print(boolean_and([True, True, True, True]))
print(boolean_and([False, True, True, True]))
print(boolean_and([False, False, False, False]))
print(boolean_and([False, False, True, True]))
Test.assert_equals(boolean_and([True, True, False, True]), False)
Test.assert_equals(boolean_and([True, True, True, True]), True)
Test.assert_equals(boolean_and([False, True, True, True]), False)
Test.assert_equals(boolean_and([False, False, False, False]), False)
Test.assert_equals(boolean_and([False, False, True, True]), False)

# OR tests
print(boolean_or([True, True, False, False]))
print(boolean_or([True, False, False, False]))
print(boolean_or([False, False, False, True, False]))
print(boolean_or([False, True, False, True, False, True]))
print(boolean_or([False, False, False, False, False]))
Test.assert_equals(boolean_or([True, True, False, False]), True)
Test.assert_equals(boolean_or([True, False, False, False]), True)
Test.assert_equals(boolean_or([False, False, False, True, False]), True)
Test.assert_equals(boolean_or([False, True, False, True, False, True]), True)
Test.assert_equals(boolean_or([False, False, False, False, False]), False)"""

# XOR tests
print(boolean_xor([True, True, False, True]))
print(boolean_xor([True, True, False, False]))
print(boolean_xor([True, False, False, False]))
print(boolean_xor([True, False, True, False]))
print(boolean_xor([True, True, True, True]))
print(boolean_xor([False, False, False, False]))
print(boolean_xor([False, False, False, True]))
print(boolean_xor([True, False, False, True]))
"""Test.assert_equals(boolean_xor([True, True, False, True]), True)
Test.assert_equals(boolean_xor([True, True, False, False]), False)
Test.assert_equals(boolean_xor([True, False, False, False]), True)
Test.assert_equals(boolean_xor([True, False, True, False]), False)
Test.assert_equals(boolean_xor([True, True, True, True]), False)
Test.assert_equals(boolean_xor([False, False, False, False]), False)
Test.assert_equals(boolean_xor([False, False, False, True]), True)
Test.assert_equals(boolean_xor([True, False, False, True]), False)"""

from functools import reduce

def boolean_and(lst):
	return reduce(lambda a, b : a & b, lst)	

def boolean_or(lst):
	return reduce(lambda a, b : a | b, lst)	

def boolean_xor(lst):
	return reduce(lambda a, b : a ^ b, lst)

def boolean_and(lst):
	return all(lst)

def boolean_or(lst):
	return any(lst)

def boolean_xor(lst):
	if lst.count(False)%2==1:
		return True
	return False