"""Help the drunken programmer fix his code! The RegEx string should be designed so it can reliably test if a string has an "A" at the beginning and end (case insensitive) as well as a "P" somewhere in between (also case insensitive).

Due to the use of fullmatch, no ending $ or beginning ^ match character is permitted anywhere except for the middle. Also, requirements have changed. Now, all characters must be allowed!
Notes

Go to the Tests tab for more help."""

import re
def regexRepairs(string):
    pattern = "(?i)a.*p.*a" #(?i) - match the remainder of the pattern with the i - insensitive modifier. "." matches any character. "*" matches previous token between zero and unlimited times, as many times as possible.  Word begins and ends with an "a" and must include a "p"

"""import re
pattern = '[Aa].*[Pp].*[Aa]'"""

