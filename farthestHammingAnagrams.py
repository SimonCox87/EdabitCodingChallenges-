# An anagram is a word, x, formed by rearranging the letters that make up another word, y, and using up all the letters in y 
# at the same frequency. For example, "dear" is an anagram of "read" and "plead" is an anagram of "paled".

# The Hamming distance between two strings is the number of positions at which they differ. Hamming distances can only be 
# calculated for strings of equal length.

# s1 = "eleven"

# s2 = "twelve"

# They only have the third position (index 2) in common, giving them a Hamming distance of 5.

# As anagrams are of identical length, the Hamming distance between them can be calculated.

# s1 = "read"

# s2 = "dear"

# These strings differ at the first and last positions, giving them a Hamming distance of 2. "Plead" and "paled" have a 
# Hamming distance of 3.

# Create a function that takes two strings, and returns:

#     True if they are anagrams of each other and their Hamming distance is equal to their length (i.e. no letters in the 
#     same positions).

#     False if they aren't anagrams, or
#     Their Hamming distance if they are anagrams with >=1 letter at the same index.

# Examples

# max_ham("dear", "read") ➞ 2

# max_ham("dare", "read") ➞ True

# max_ham("solemn", "molest") ➞ False

#My original solution
def max_ham(s1, s2):
    ham = sum(a!=b for a,b in zip(s1,s2))
    s = sorted(s1)==sorted(s2)
    return True if ham==len(s1) and s else ham if s else False

#Solution to filter out non-anagrams
# def max_ham(s1,s2):
#     if sorted(s1)!=sorted(s2):
#         return False
#     ham = sum(a!=b for a,b in zip(s1,s2))
#     return ham==len(s1) or ham

print(max_ham('dare','read')) #, True)
print(max_ham('dear','read')) #, 2)
print(max_ham('naive','ravine')) #, False)
print(max_ham('observe','verbose')) #, 6)
print(max_ham('mister','remits')) #, True)
print(max_ham('pirates','traipse')) #, True)
print(max_ham('petal','leapt')) #, 4)
print(max_ham('solemn','molest')) #, False)
print(max_ham('solemn','melons')) #, 5)
print(max_ham('solemn','lemons')) #, True)
print(max_ham('emigrants','streaming')) #, True)
print(max_ham('teardrop','predated')) #, False)

	