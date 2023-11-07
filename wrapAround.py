"""Create a function to reproduce the wrap around effect shown:
Examples

wrap_around("Hello, World!", 2) ➞ "llo, World!He"

wrap_around("From what I gathered", -4) ➞ "eredFrom what I gath"

wrap_around("Excelsior", 30) ➞ "elsiorExc"

wrap_around("Nonscience", -116) ➞ "cienceNons"

Notes

    The offset can be negative.
    The offset can be greater than the length of string."""

def wrap_around(string, offset):
    # cut = offset % len(string)
    # return string[cut:] + string[:cut]
    return string[offset%len(string):] + string[:offset%len(string)]

"""print(wrap_around("Hello, World!", 2)) # ➞ "llo, World!He"
print(wrap_around("From what I gathered", -4)) # ➞ "eredFrom what I gath"
print(wrap_around("Excelsior", 30)) # ➞ "elsiorExc"
print(wrap_around("Nonscience", -116)) # ➞ "cienceNons"""

print(wrap_around("Hello, World!", 2,)) #, "llo, World!He")
print(wrap_around("From what I gathered", -4)) #, "eredFrom what I gath")
print(wrap_around("No Changes", 0)) #, "No Changes")
print(wrap_around("S", -60)) #, "S")
print(wrap_around("Subordinating", 2)) #, "bordinatingSu")
print(wrap_around("Assemblywomen", -6)) #, "ywomenAssembl")
print(wrap_around("Pedantic", 4)) #, "nticPeda")
print(wrap_around("Nonscience", -116)) #, "cienceNons")
print(wrap_around("Excelsior", 30)) #, "elsiorExc")
print(wrap_around("Incomprehensibilities", 50)) #, "hensibilitiesIncompre")

