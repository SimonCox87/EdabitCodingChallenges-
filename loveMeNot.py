""""Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.
Examples

loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"

Notes

    Remember to return a string.
    The first phrase is always "Loves me"."""

def loves_me(n):
    lst = ["Loves me" if i % 2 == 0 else "Loves me not" for i in range(n)]
    return ", ".join(lst[0:-1]) + ", " + lst[-1].upper() if len(lst) > 1 else lst[-1].upper()

print(loves_me(3))
print(loves_me(6))
print(loves_me(1))

def loves_me(n):
    lst = ["Loves me" if i % 2 == 0 else "Loves me not" for i in range(n)]
    lst[-1] = lst[-1].upper()
    return ", ".join(lst)

print(loves_me(3))
print(loves_me(6))
print(loves_me(1))

"""def loves_me(n):
    arr = (['Loves me', 'Loves me not']*n)[:n]
    arr[-1] = arr[-1].upper()
    return ', '.join(arr)"""

"""def loves_me(n):
	a=["Loves me"+" not"*(i%2) for i in range(n)]
	a[-1]=a[-1].upper()
	return ", ".join(a)"""
