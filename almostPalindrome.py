# A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function 
# that returns True if a string is an almost-palindrome and False otherwise.

# Examples

# almost_palindrome("abcdcbg") ➞ True
# # Transformed to "abcdcba" by changing "g" to "a".

# almost_palindrome("abccia") ➞ True
# # Transformed to "abccba" by changing "i" to "b".

# almost_palindrome("abcdaaa") ➞ False
# # Can't be transformed to a palindrome in exactly 1 turn.

# almost_palindrome("1234312") ➞ False

# Notes

# Return False if the string is already a palindrome.

def almost_palindrome(txt): 
    sl = len(txt)//2+1
    return sum(txt[:sl][i] != txt[::-1][:sl][i] for i in range(sl)) == 1
    

# print(almost_palindrome("abcdcbg")) # ➞ True
# # Transformed to "abcdcba" by changing "g" to "a".

# print(almost_palindrome("abccia")) # ➞ True
# # Transformed to "abccba" by changing "i" to "b".

# print(almost_palindrome("abcdaaa")) # ➞ False
# # Can't be transformed to a palindrome in exactly 1 turn.

# print(almost_palindrome("1234312")) # ➞ False

print(almost_palindrome("abcdcbg")) #, True)
print(almost_palindrome("abccia")) #, True)
print(almost_palindrome("abcdaaa")) #, False)
print(almost_palindrome("gggfgig")) #, True)
print(almost_palindrome("gggffff")) #, False)
print(almost_palindrome("GIGGG")) #, True)
print(almost_palindrome("ggggi")) #, True)
print(almost_palindrome("ggggg")) #, False, 'Should return false if already palindrome.')
print(almost_palindrome("gggfggg")) #, False, 'Should return false if already palindrome.')
print(almost_palindrome("1234312")) #, False)

# def almost_palindrome(txt):
# 	return sum(a != b for a, b in zip(txt, txt[::-1])) == 2

# def almost_palindrome(txt):
# 	return sum(1 for i in range(len(txt)) if txt[i] != txt[-1-i]) == 2
