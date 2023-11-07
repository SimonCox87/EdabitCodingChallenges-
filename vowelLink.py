"""Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word 
immediately after begins with a vowel (a e i o u).
Examples

vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False

Notes

You can expect sentences in only lowercase, with no punctuation."""
import re
def vowel_links(txt):
    return True if re.search("[aeiou]\s[aeiou]", txt) else False
    
print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
print(vowel_links("a sudden applause"))

"""import re

def vowel_links(txt):
	return bool(re.search('[aeiou] [aeiou]', txt))"""

"""def vowel_links(txt):
  l, v = txt.split(), 'aeuio'
  return any(l[i][-1] in v and l[i+1][0] in v for i in range(len(l)-1))"""

"""import re
vowel_links=lambda t:len(re.findall('[aeiou] [aeiou]',t))>0"""

"""def vowel_links(txt):
	txt, vow = txt.split(), 'aeiou'
	return any(x[-1] in vow and y[0] in vow for x, y in zip(txt, txt[1:]))"""
