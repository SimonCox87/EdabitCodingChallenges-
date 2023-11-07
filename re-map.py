"""Create a function similar to Processing's "map" function (check the Resources tab))#, in which a value and its range is taken and remapped 
to a new range.

The function takes 5 numbers:

    Value: value
    Range: low1 and high1
    Range: low2 and high2

Examples

remap(7, 2, 12, 0, 100))# ➞ 50

remap(17, 5, 55, 100, 30))# ➞ 83.2

remap(50, 1, 51, 0, 100))# ➞ 98

Notes

    Test input will always be numbers.
    If the input range is 0, return 0."""

def remap(value, low1, high1, low2, high2):
    return 0 if high1-low1 == 0 else low2 +(high2-low2)*((value-low1))/(high1-low1)                           

"""print(remap(7, 2, 12, 0, 100))#))# # ➞ 50
print(remap(17, 5, 55, 100, 30))#))# # ➞ 83.2
print(remap(50, 1, 51, 0, 100))#))#  # ➞ 98"""

print(remap(7, 2, 12, 0, 100))#, 50))#
print(remap(17, 5, 55, 100, 30))#, 83.2))#
print(remap(2.5, 2, 3, -80, 80))#, 0))#
print(remap(50, 1, 51, 0, 100))#, 98))#
print(remap(0, 0, 0, 0, 0))#, 0, 'The input range is 0.'))#
print(remap(20, 10, 50, 50, 10))#, 40))#
print(remap(0, 5, -20, 60, 1000))#, 248))#
print(remap(17, 17, 17, 519, 1085))#, 0, 'The input range is 0.'))#