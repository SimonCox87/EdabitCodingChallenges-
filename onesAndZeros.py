# Write a function that returns True if every consecutive sequence of ones is followed by a consecutive sequence of zeroes of 
# the same length.

# Examples

# same_length("110011100010") ➞ True

# same_length("101010110") ➞ False

# same_length("111100001100") ➞ True

# same_length("111") ➞ False

from itertools import zip_longest as zl
def same_length(txt):
    z = zl(filter(lambda x: x!="",txt.split("0")), filter(lambda x: x!="",txt.split("1")),fillvalue="")
    return all(len(a)==len(b) for a,b in z)

# print(same_length("110011100010")) # ➞ True
# print(same_length("101010110")) # ➞ False
# print(same_length("111100001100")) # ➞ True
# print(same_length("111")) # ➞ False

print(same_length('10'))# True)
print(same_length('1010'))#, True)
print(same_length('1100'))#, True)
print(same_length('10101110001100'))#, True)
print(same_length('1111000010101100'))#, True)
print("\n")
print(same_length('1001'))#, False)
print(same_length('101001'))#, False)
print(same_length('101'))#, False)
print(same_length('10010'))#, False)
print(same_length('110'))#, False)
print(same_length('11001'))#, False)
print(same_length('11100011000'))#, False)

# import re
# def same_length(txt):
# 	return all(len(a)==len(b) for a,b in zip(re.findall(r'1+',txt),re.findall(r'0+',txt))) and txt[-1]!='1'

# def same_length(txt):
#     while '10' in txt:
#         txt = txt.replace('10', '')
#     return len(txt) == 0

# import re
# def same_length(txt):
# 	return [len(i) for i in re.findall('1+',txt)]==[len(i) for i in re.findall('0+',txt)]
	