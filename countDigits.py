"""Create a function that counts the number of digits in a number. Conversion of the number to a string is not allowed.
Examples

digits_count(4666) ➞ 4

digits_count(544) ➞ 3

digits_count(121317) ➞ 6

digits_count(0) ➞ 1

digits_count(12345) ➞ 5

digits_count(1289396387328) ➞ 13

Notes

    All inputs are integers but some are in exponential form, deal with it accordingly."""

def digits_count(n):
    digits = 0
    if n == 0:
        digits = 1
    while n != 0:
        n //= 10
        digits += 1
    
    return digits
    
print(digits_count(4666))
print(digits_count(544))
print(digits_count(121317))
print(digits_count(0))
print(digits_count(12345))
print(digits_count(1289396387328))

"""def digits_count(n):
    if n // 10 == 0:
        return 1
    return 1 + digits_count(n // 10)

print(digits_count(4666))
print(digits_count(544))
print(digits_count(121317))
print(digits_count(0))
print(digits_count(12345))
print(digits_count(1289396387328))"""

"""def digits_count(n):
    '''
    Returns a count of the digits in integer n
    '''
    counter = lambda x: 1 if x < 10 else 1 + counter(x//10)

    return counter(int(abs(n)))"""

"""import math
def digits_count(n):
	return 1 if n == 0 else math.ceil(math.log10(abs(n)))"""

"""def digits_count(n):
	return 1 if abs(n)<10 else 1+ digits_count (n//10)"""
