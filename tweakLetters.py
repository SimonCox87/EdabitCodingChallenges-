# Create a function that tweaks letters by one forward (+1) or backwards (-1) according to a list.
# Examples

# tweak_letters("apple", [0, 1, -1, 0, -1]) ➞ "aqold"
# # "p" + 1 => "q"; "p" - 1 => "o"; "e" - 1 => "d"

# tweak_letters("many", [0, 0, 0, -1]) ➞ "manx"

# tweak_letters("rhino", [1, 1, 1, 1, 1]) ➞ "sijop"

# Notes

# Don't worry about capital letters.

def tweak_letters(txt, lst):
    return "".join([chr(ord(txt[i]) + lst[i]) for i in range(len(txt))]).replace("{","a").replace("`","z")

# print(tweak_letters("apple", [0, 1, -1, 0, -1])) # ➞ "aqold"
# # "p" + 1 => "q"; "p" - 1 => "o"; "e" - 1 => "d"
# print(tweak_letters("many", [0, 0, 0, -1])) # ➞ "manx"
# print(tweak_letters("rhino", [1, 1, 1, 1, 1])) # ➞ "sijop"

# a= 97, z = 122

print(tweak_letters("apple", [0, 1, -1, 0, -1])) #, "aqold")
print(tweak_letters("many", [0, 0, 0, -1])) #, "manx")
print(tweak_letters("rhino", [1, 1, 1, 1, 1])) #, "sijop")
print(tweak_letters('xyz', [1, 1, 1])) #, 'yza')
print(tweak_letters('abc', [-1, -1, -1])) #, 'zab')

# l = 'abcdefghijklmnopqrstuvwxyz'
# def tweak_letters(txt, lst):
# 	return ''.join([l[(l.find(txt[i]) + lst[i])%26] for i in range(len(lst))])

# from string import ascii_lowercase as abc
# def tweak_letters(txt, lst):
# 	return "".join([abc[(abc.index(a)+b)%26]for a, b in zip(list(txt), lst)])