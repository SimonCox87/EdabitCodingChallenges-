# Given a string, reverse its order, change lowercase letters to uppercase and increment uppercase letters by one (e.g. A becomes B, 
# C becomes D, Z becomes A).

# Examples

# change_string("ApPle") ➞ "ELQPB"

# change_string("draGON") ➞ "OPHARD"

# change_string("ZebrA") ➞ "BRBEA"

# Notes

# Remember capital "Z" becomes "A".

def change_string(word):
    return "".join(chr(ord(i) + 1) if i.isupper() else i.upper() for i in word)[::-1].replace("[","A")

print(change_string("ApPle")) # ➞ "ELQPB"
print(change_string("draGON")) # ➞ "OPHARD"
print(change_string("ZebrA")) # ➞ "BRBEA"

