# Create a function that takes a string and determine if it's a valid sequence by either returning True or False. The string 
# will be composed of + and = symbols with several characters between them (e.g. "++d+===+c++==a") and for the string to be True, each 
# letter must be surrounded by a + symbol. So the string to the left would be False.

# Examples

# simple_symbols("f++d+") ➞ False

# simple_symbols("+d+=3=+s+") ➞ True

# simple_symbols("==+p+++++++++====8+z++++") ➞ True

# Notes

# The given string will not be empty and will have at least one letter.

from re import findall as f
def simple_symbols(txt):
	return len(f(r"(?i)\+[a-z]\+",txt)) == len(f("(?i)[a-z]",txt))

print(simple_symbols("f++d+")) # ➞ False
print(simple_symbols("+d+=3=+s+")) # ➞ True
print(simple_symbols("==+p+++++++++====8+z++++")) # ➞ True
print(simple_symbols("+3+"))