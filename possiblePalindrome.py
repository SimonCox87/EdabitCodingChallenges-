# Create a function that determines whether it is possible to build a palindrome from the characters in a string.
# Examples

# possible_palindrome("acabbaa") ➞ True
# # Can make the following palindrome: "aabcbaa"

# possible_palindrome("aacbdbc") ➞ True
# # Can make the following palindrome: "abcdcba"

# possible_palindrome("aacbdb") ➞ False

# possible_palindrome("abacbb") ➞ False

def possible_palindrome(txt):
	return len(list(filter(lambda x: x%2,[txt.count(i) for i in set(txt)]))) <= 1

# print(possible_palindrome("aacbdbc")) # ➞ True
# # Can make the following palindrome: "abcdcba"
# print(possible_palindrome("aacbdb")) # ➞ False
# print(possible_palindrome("abacbb")) # ➞ False

print(possible_palindrome("acabbaa")) #, True)
print(possible_palindrome("aacbdbc")) #, True)
print(possible_palindrome("aacbdb")) #, False)
print(possible_palindrome("abacbb")) #, False)
print(possible_palindrome("abb")) #, True)
print(possible_palindrome("bbb")) #, True)
print(possible_palindrome("bbaa")) #, True)
print(possible_palindrome("bbaacc")) #, True)
print(possible_palindrome("bbaaccd")) #, True)
print(possible_palindrome("bbaacd")) #, False)
print(possible_palindrome("abc")) #, False)
print(possible_palindrome("ab")) #, False)
print(possible_palindrome("aabbccddef")) #, False)

def possible_palindrome(txt):
	return sum(txt.count(i)%2 for i in set(txt)) <= 1