"""Create a class with a few functions like these examples.

    Magic
.replace("string", 'char', char') is a function that replaces all of the specified characters with different specified characters.
    Magic
.str_length("string") is a function that returns the length of the string.
    Magic
.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
    Magic
.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes. If the length of 
    the new list is 0, return -1.

Examples

Magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"

Magic.str_length("hello world") ➞ 11

Magic.trim("      python is awesome      ") ➞ "python is awesome"

Magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]"""

class magic:
    def __init__(self):
        pass

    def replace(self, string, char1, char2):
        return string.replace(char1, char2)
    
    def str_length(self, string):
        return len(string)
    
    def trim(self, string):
        return string.strip()
    
    def list_slice(self, list, tuple):
        return list[tuple[0]-1:tuple[1]] if len(list[tuple[0]-1:tuple[1]]) > 0 else -1

magic = magic()
print(magic.replace("AzErty-QwErty", "E", "e")) #"Azerty-Qwerty"
print(magic.str_length("hello world")) #11
print(magic.trim("      python is awesome      ")) #"python is awesome"
print(magic.list_slice([1, 2, 3, 4, 5], (2, 4))) #[ 2, 3, 4 ]

"""class Magic:
    def replace(self,string,char1,char2):
        return string.replace(char1,char2)

    def str_length(self,string):
        return len(string)

    def trim(self,string):
        return string.strip()

    def list_slice(self,string,tup):
        return string[tup[0]-1:tup[1]] if len(string[tup[0]-1:tup[1]]) > 0 else -1"""
