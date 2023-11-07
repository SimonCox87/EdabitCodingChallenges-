# Given a sentence, return the number of words which have the same first and last letter.
# Examples

# count_same_ends("Pop! goes the balloon") ➞ 1

# count_same_ends("And the crowd goes wild!") ➞ 0

# count_same_ends("No I am not in a gang.") ➞ 1

# Notes

#     Don't count single character words (such as "I" and "A" in example #3).
#     The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
#     Mind the punctuation!
#     Bonus points indeed for using regex!

import re
def count_same_ends(txt):
    return len([i for i in re.sub('\W'," ",txt).lower().split() if i[0]==i[-1] and len(i)>1])

print(count_same_ends("Pop! goes the balloon")) # ➞ 1
print(count_same_ends("And the crowd goes wild!")) # ➞ 0
print(count_same_ends("No I am not in a gang.")) # ➞ 1

# re.sub(r'[^\w\s]',"",txt)

# import re
# def count_same_ends(txt):
# 	return sum((w[0]==w[-1] and len(w)>1) for w in re.findall(r'\w+',txt.lower()))

# import re

# def count_same_ends(txt):
# 	return len(re.findall(r'\b(\w)\w*\1\b', txt.lower()))