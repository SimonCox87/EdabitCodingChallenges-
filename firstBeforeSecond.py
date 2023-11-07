"""You are given three inputs: a string, one letter, and a second letter.

Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.
Examples

first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
# Every instance of "a" occurs before every instance of "j".

first_before_second("knaves knew about waterfalls", "k", "w") ➞  True

first_before_second("happy birthday", "a", "y") ➞ False
# The "a" in "birthday" occurs after the "y" in "happy".

first_before_second("precarious kangaroos", "k", "a") ➞ False

Notes

    All strings will be in lower case.
    All strings will contain the first and second letters at least once."""

def first_before_second(s, first, second):
    return s.rindex(first) < s.index(second)

print(first_before_second("a rabbit jumps joyfully", "a", "j")) # True
print(first_before_second("knaves knew about waterfalls", "k", "w")) # True
print(first_before_second("maria makes money", "m", "o")) #True
print(first_before_second("the hostess made pecan pie", "h", "p")) #True
print(first_before_second("barry the butterfly flew away", "b", "f")) #True
print(first_before_second("moody muggles", "m", "g")) #True

print(first_before_second("happy birthday", "a", "y")) #False
print(first_before_second("precarious kangaroos", "k", "a")) #False
print(first_before_second("maria makes money", "m", "i")) #False
print(first_before_second("taken by the beautiful sunrise", "u", "s")) #False
print(first_before_second("sharp cheddar biscuit", "t", "s")) #False
print(first_before_second("moody muggles", "m", "o")) #False