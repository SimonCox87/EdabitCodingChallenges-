"""Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a 
string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.
Examples

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


alphabet_index(alphabet, "Flavio") ➞ "22v"

alphabet_index(alphabet, "Andrey") ➞ "25y"

alphabet_index(alphabet, "Oscar") ➞ "19s"

Notes

    If you're stuck, check the Resources tab.
    sorted() is not best practice."""

alphabet = []
def alphabet_index(alphabet, string):
    strLst = [c for c in string.lower()]
    strLst.sort()
    return str(ord(strLst[-1]) - 96) + strLst[-1]
print(alphabet_index(alphabet, "Flavio"))

"""alphabet = []
def alphabet_index(*args):
    res, max_idx = "a", 97
    for c in args[1].lower():
        idx = ord(c)
        if idx > max_idx:
            res = "{}{}".format(idx - 96, c)
            max_idx = idx
    return res"""

"""alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def alphabet_index(alphabet, string):
    n = 0; r = {i:{i:index + 1 for index, i in enumerate(alphabet)}[i] for i in string.lower()}
    for i, j in r.items():
        if j > n: n = j
    for i in r:
        if r[i] == n: return "{0} * {1}".format(i, n)

print(alphabet(alphabet, "Flavio"))"""



