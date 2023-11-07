# Write a function that returns True if it's possible to build a phrase txt1 using only the characters from another phrase txt2.
# Examples

# can_build("got 2 go", "gogogo 2 today") ➞ True

# can_build("sit on top", "its a moo point") ➞ True

# can_build("long high add or", "highway road go long") ➞ False

# can_build("fill tuck mid", "truck falls dim") ➞ False

# Notes

#     All letters will be in lower case.
#     Numbers and special characters included.
#     Ignore whitespaces.
#     Do not count white space as a character.

# def can_build(txt1, txt2):
# 	txt1,txt2 = txt1.replace(" ",""),txt2.replace(" ","")
# 	return all(txt1.count(i) <= txt2.count(i) for i in txt1)

def can_build(txt1, txt2):
    txt1,txt2 = "".join(txt1.split()),"".join(txt2.split())
    return all(txt1.count(i) <= txt2.count(i) for i in set(txt1))


# print(can_build("got 2 go", "gogogo 2 today")) # ➞ True
# print(can_build("sit on top", "its a moo point")) # ➞ True
# print(can_build("long high add or", "highway road go long")) # ➞ False
# print(can_build("fill tuck mid", "truck falls dim")) # ➞ False

print(can_build("got 2 go", "go go go 2 today")) #, True)
print(can_build("for an angel", "angel forest nymph awaken")) #, True)
print(can_build("sit on top", "its a moo point")) #, True)
print(can_build("solar to oven", "love desolate rose thorn")) #, True)
print(can_build("gate im in", "magnetizing")) #, True)
print(can_build("moreso", "mount rushmore")) #, True)
print(can_build("dool", "ken doll")) #, False)
print(can_build("world of make believe", "make believe world")) #, False)
print(can_build("long high add or", "highway road go long")) #, False)
print(can_build("fill tuck mid", "truck falls dim")) #, False)
print(can_build("skin man i", "man in mask")) #, False)
print(can_build("foolish prides", "foolish pride")) #, False)

#iterating from a set could be faster than my code

# def can_build(txt1, txt2):
# 	return all(txt2.count(i) >= txt1.count(i) for i in set(txt1) if i.isalpha()) # think is alpha() method creates an incorrect solution here