# Write a regular expression that will help us count how many bad cookies are produced every day. You must use RegEx negative 
# lookbehind.

# Example

# lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
# pattern = "yourregularexpressionhere"

# len(re.findall(pattern, ", ".join(lst))) ➞ 2

import re

lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = 'bad(?<! )'

print(len(re.findall(pattern, ", ".join(lst)))) # ➞ 2