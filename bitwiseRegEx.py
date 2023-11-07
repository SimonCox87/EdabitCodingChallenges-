"""Create two functions:

    The first is is_odd() to check if a given number is odd using bitwise operator.
    The second is is_even() to check if a given input is even using regular expressions.

Use of % operator is disallowed.
Examples

is_odd(3) ➞ "Yes"
# Use Bitwise Operator

is_odd(58) ➞ "No"
# Use Bitwise Operator

is_even("0") ➞ "Yes"
# Use Regular Expression

is_even("-99") ➞ "No"
# Use Regular Expression

Notes

    Input will only be integers (positive/negative/zero).
    For the second function, input will be numbers in string.
    For more info on regular expressions, check the Resources tab."""

import re
# Use Bitwise Operator (% modulo operator disallowed)
def is_odd(n):
    return "Yes" if n & 1 else "No"
	

# Use Regular Expression (% modulo operator disallowed)
def is_even(n):
    return "Yes" if re.search('[02468]$',n) else "No" 

print(is_odd(-7)) #, "Yes")
print(is_odd(-5)) #, "Yes")
print(is_odd(17)) #, "Yes")
print(is_odd(-6)) #, "No")
print(is_odd(0)) #, "No")
print("\n")
print(is_even("-7")) #, "No")
print(is_even("111")) #, "No")
print(is_even("0")) #, "Yes")
print(is_even("-12")) #, "Yes")
print(is_even("40")) #, "Yes")


#Bitwise Operator Xor
# "Yes" if n ^ 1 == n - 1 else "No"
#Bitwise Or
# "Yes" if n | 1 == n else "No"
#Bitwise Left and Right shift operators
# "Yes" if n == (n >> 1) << 1 else "No"