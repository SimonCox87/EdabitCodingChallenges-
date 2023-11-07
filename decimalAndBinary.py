"""A number/string is a palindrome if the digits/characters are the same when read both forward and backward. Examples include 
"racecar" and 12321. Given a positive number n, check if n or the binary representation of n is palindromic. Return the following:

    "Decimal only." if only n is a palindrome.
    "Binary only." if only the binary representation of n is a palindrome.
    "Decimal and binary." if both are palindromes.
    "Neither!" if neither are palindromes.

Examples

palindrome_type(1306031) ➞ "Decimal only."
# decimal = 1306031
# binary  = "100111110110110101111"

palindrome_type(427787) ➞ "Binary only."
# decimal = 427787
# binary  = "1101000011100001011"

palindrome_type(313) ➞ "Decimal and binary."
# decimal = 313
# binary  = 100111001

palindrome_type(934) ➞ "Neither!"
# decimal = 934
# binary  = "1110100110"""

def palindrome_type(n):
    n = str(n)
    b = bin(int(n))[2:]
    if n==n[::-1] and b==b[::-1]:
        return "Decimal and binary."
    elif b==b[::-1]: 
        return "Binary only."
    elif n==n[::-1]:
        return "Decimal only."
    return "Neither!"

print(palindrome_type(1934391)) #, "Decimal and binary.")
print(palindrome_type(9994521)) #, "Binary only.")
print(palindrome_type(5841485)) #, "Decimal and binary.")
print(palindrome_type(8337738)) #, "Neither!")
print(palindrome_type(7447)) #, "Decimal and binary.")
print(palindrome_type(18985)) #, "Binary only.")
print(palindrome_type(7)) #, "Decimal and binary.")
print(palindrome_type(1306031)) #, "Decimal only.")
print(palindrome_type(1)) #, "Decimal and binary.")
print(palindrome_type(1903127)) #, "Binary only.")
print(palindrome_type(4)) #, "Decimal only.")
print(palindrome_type(48084)) #, "Decimal only.")
print(palindrome_type(427787)) #, "Binary only.")
print(palindrome_type(456)) #, "Neither!")
print(palindrome_type(313)) #, "Decimal and binary.")
print(palindrome_type(3664663)) #, "Decimal only.")
print(palindrome_type(585585)) #, "Decimal and binary.")
print(palindrome_type(14441)) #, "Decimal only.")
print(palindrome_type(8494948)) #, "Decimal only.")
print(palindrome_type(932)) #, "Neither!")
print(palindrome_type(7115931)) #, "Binary only.")
print(palindrome_type(101)) #, "Decimal only.")
print(palindrome_type(6286333)) #, "Binary only.")

"""def palindrome_type(n):
	b, d = [s == s[::-1] for s in [str(n), bin(n)[2:]]]
	return ['Neither!','Binary only.','Decimal only.','Decimal and binary.'][d + 2 * b]

def palindrome_type(n):
	s=["Neither!","Decimal only.","Binary only.","Decimal and binary."]
	i=0
	
	a=str(n)
	if a==a[::-1]:
		i+=1
	b=bin(n)[2:]
	if b==b[::-1]:
		i+=2
	return s[i]"""