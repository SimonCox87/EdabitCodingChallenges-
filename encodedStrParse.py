"""Create a function which takes in an encoded string and returns a dictionary according to the following example:
Examples

parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}

Notes

    The string will always be in the same format: first name, last name and id with zeros between them.
    id numbers will not contain any zeros.
    Bonus: Try solving this using RegEx."""

"""def parse_code(txt):
    for char in txt:
        if char == "0":
            txt = txt.replace(char, " ")
    keys = ["first_name", "last_name", "id"]
    return dict(zip(keys, txt.split()))

    print(parse_code("John000Doe000123"))
    print(parse_code("michael0smith004331"))
    print(parse_code("Thomas00LEE0000043"))"""

import re
def parse_code(txt):
    keys = ["first_name", "last_name", "id"]
    return dict(zip(keys, re.split("0+", txt)))

print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))

"""import re

def parse_code(txt):
	first, second, _id = re.split('0+', txt)
	return {'first_name': first, 'last_name': second, 'id': _id}"""

"""import re

def parse_code(txt):
	return dict(zip(('first_name', 'last_name', 'id'), re.split('0+', txt)))"""


