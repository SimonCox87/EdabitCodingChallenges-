"""Create a function that takes in two words as input and returns a list of three elements, in the following order:

    Shared letters between two words.
    Letters unique to word 1.
    Letters unique to word 2.

Each element should have unique letters, and have each letter be alphabetically sorted.
Examples

letters("sharp", "soap") ➞ ["aps", "hr", "o"]

letters("board", "bored") ➞ ["bdor", "a", "e"]

letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]

letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# Even with multiple matching letters (e.g. 3 f's), there should 
# only exist a single "f" in your first element.

letters("match", "ham") ➞ ["ahm", "ct", ""]
# "ham" does not contain any letters that are not found already 
# in "match".

Notes

    Both words will be in lower case.
    You do not have to worry about punctuation, all words only have letters from [a-z].
    If an element contains no letters, return an empty string (see last example)."""

def letters(word1, word2):
    shared = "".join(sorted(set(i for i in word1 if i in word2)))
    unique1 = "".join(sorted(set(i for i in word1 if i not in word2)))
    unique2 = "".join(sorted(set(i for i in word2 if i not in word1)))
    return[shared, unique1, unique2]

print(letters("sharp", "soap"))
print(letters("board", "bored"))
print(letters("happiness", "envelope"))
print(letters("kerfuffle", "fluffy"))
print(letters("match", "ham"))

"""def letters(word1, word2):
	s1, s2 = set(word1), set(word2)
	return [''.join(sorted(i)) for i in [s1&s2, s1-s2, s2-s1]]

https://www.programiz.com/python-programming/set"""
