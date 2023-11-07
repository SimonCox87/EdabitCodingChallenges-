"""Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two lines rhyme if the 
last word from each sentence contains the same vowels.
Examples

does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True

does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
# Capitalization and punctuation should not matter.

does_rhyme("You are off to the races", "a splendid day.") ➞ False

does_rhyme("and frequently do?", "you gotta move.") ➞ False

Notes

    Case insensitive.
    Here we are disregarding cases like "thyme" and "lime".
    We are also disregarding cases like "away" and "today" (which technically rhyme, even though they contain different vowels)."""

def does_rhyme(txt1, txt2):
    l1 = [i for i in txt1.split()[-1].lower() if i in ["a","e","i","o","u"]] # could just use a string "aeiou" instead of the list
    l2 = [i for i in txt2.split()[-1].lower() if i in ["a","e","i","o","u"]]
    return l1 == l2

print(does_rhyme("Sam I am!", "Green eggs and ham."))
print(does_rhyme("Sam I am!", "Green eggs and HAM."))
print(does_rhyme("You are off to the races", "a splendid day."))
print(does_rhyme("and frequently do?", "you gotta move."))

"""import re
def does_rhyme(str_1, str_2):								# Rhyme Time
	str_1, str_2 = str_1.lower().split()[-1], str_2.lower().split()[-1]
	return re.findall(r'[aeiou]', str_1) == re.findall(r'[aeiou]', str_2)""" 


