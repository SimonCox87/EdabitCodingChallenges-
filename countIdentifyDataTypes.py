"""Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally 
return the total in a list.

List order is:

[int, str, bool, list, tuple, dictionary]

Examples

count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]

count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]

count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]

count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]

Notes

If no arguments are given, return [0, 0, 0, 0, 0, 0]"""
#original version that i created.  Python 3.10.6 creates ordered dictionaries by default.
def count_datatypes(*args):
    dataTypes = {int: 0, str: 0, bool: 0, list: 0, tuple: 0, dict: 0}
    
    for t in dataTypes:
        for i in args:
            if type(i) == t:
                dataTypes[t] +=1
        
    return[dataTypes[i] for i in dataTypes]            


print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))

#More compact version of my code
def count_datatypes(*args):
    dataTypes = {int: 0, str: 0, bool: 0, list: 0, tuple: 0, dict: 0}
    for i in args:
        if type(i) in dataTypes:
            dataTypes[type(i)] += 1
    return list(dataTypes.values())

print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))

"""from collections import OrderedDict
def count_datatypes(*args):
    dataTypes= OrderedDict([(int, 0),(str,0),(bool,0),(list,0),(tuple,0),(dict,0)])
    for i in args:
        if type(i) in dataTypes:
            dataTypes[type(i)] += 1
    return list(dataTypes.values())

print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))

def count_datatypes(*args):
    lst = [type(i) for i in args]
    return [lst.count(i) for i in (int, str, bool, list, tuple, dict)]

def count_datatypes(*args):
	types = [int, str, bool, list, tuple, dict]
	return [sum(type(i) is t for i in args) for t in types]"""