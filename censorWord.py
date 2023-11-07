"""Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the 
given character char.
Examples

censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"""

def censor_string(txt, lst, char):
    for i in lst:
        txt = txt.replace(i, char * len(i), 1)
    return txt

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))

"""def censor_string(txt, lst, char):
	return ' '.join(char*len(word) if word in lst else word for word in txt.split())"""

"""import re
def censor_string(txt, lst, char):
	return re.sub(r' ([,.?!])', r' \1', ''.join([char * len(word) + ' ' if word.lower() in (a.lower() for a in lst) else word + ' ' for word in re.sub( r'([,.?!])', r'\1',txt).split()]).strip())"""