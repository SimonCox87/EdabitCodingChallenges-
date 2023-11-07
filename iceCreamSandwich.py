# An ice cream sandwich is a string that is formed by two identical ends and a different middle.
# Some examples of ice cream sandwiches:

# "AABBBAA"

# "3&&3"

# "yyyyymmmmmmmmyyyyy"

# "hhhhhhhhmhhhhhhhh"

# Notice how left and right ends of the sandwich are identical in both length and in repeating character). The middle section is 
# distinctly different.

# Not ice cream sandwiches:

# "BBBBB"
# // You can't have just plain icecream.

# "AAACCCAA"
# // You can't have unequal sandwich ends.

# "AACDCAA"
# // You can't have more than one filling.

# "A"
# // You can't have fewer than 3 characters.

# Write a function that returns True if a string is an ice cream sandwich and False otherwise.
# Examples

# is_icecream_sandwich("CDC") ➞ True

# is_icecream_sandwich("AAABB") ➞ False

# is_icecream_sandwich("AA") ➞ False

# Notes

# An ice cream sandwich must have a minimum length of 3 characters, and at least two of these characters must be distinct 
# (you can't only have the filling!).

def is_icecream_sandwich(txt):
    if len(txt)<3 or len(set(txt))>2:
        return False
    t = "".join([txt[i]+" " if txt[i]!=txt[i+1] else txt[i] for i in range(len(txt)-1)]+[txt[-1]]).split()
    return len(t) == 3 and t[0] == t[2]

# print(is_icecream_sandwich("CDC")) # ➞ True
# print(is_icecream_sandwich("AAABB")) # ➞ False
# print(is_icecream_sandwich("AA")) # ➞ False

print(is_icecream_sandwich("")) # False, "too short")
print(is_icecream_sandwich("AABBBAA")) # True)
print(is_icecream_sandwich("3&&3")) # True)
print(is_icecream_sandwich("yyyyymmmmmmmmyyyyy")) # True)
print(is_icecream_sandwich("hhhhhhhhmhhhhhhhh")) # True)
print(is_icecream_sandwich("CDC")) # True)
print(is_icecream_sandwich("BBBBB")) # False, "only filling")
print(is_icecream_sandwich("AAACCCAA")) # False, "ends are unbalanced")
print(is_icecream_sandwich("AACDCAA")) # False, "can only have one type of filling")
print(is_icecream_sandwich("AAABB")) # False, "only one end")
print(is_icecream_sandwich("AA")) # False, "too short")
print(is_icecream_sandwich("A")) # False, "too short"
print(is_icecream_sandwich("AAABBABBAAA"))

# from itertools import groupby

# def is_icecream_sandwich(txt):
# 	return txt == txt[::-1] and len(list(groupby(txt))) == 3