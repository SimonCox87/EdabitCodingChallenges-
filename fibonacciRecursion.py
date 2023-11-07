"""The Fibonacci sequence is a classic use case for recursive functions since the value of the sequence at a given index is 
dependent on the sum of the last two values. However, the recursion tree created by solving the Fibonacci sequence recursively 
can grow quite fast. Therefore it can be important to think about the implications of running a function recursively. Depending on 
the size of n needed and the capabilities of the system in question you might want to take a different approach.

Write a non-recursive function that takes an integer n and returns the Fibonacci sequence's value at index n.

Examples

fib(6) ➞ 8
# 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

fib(1) ➞ 1

fib(2) ➞ 1

0, 1, 1, 2, 3, 5, 8, 13, 21, 34,"""

def fib(n):
    a, b = 0, 1
    if n == 0:
        return a
    for i in range(n-1):
        a, b = b, a + b
    return b

print(fib(0)) #, 0)
print(fib(1)) #, 1)
print(fib(2)) #, 1)
print(fib(3)) #, 2)
print(fib(4)) #, 3)
print(fib(5)) #, 5)
print(fib(6)) #, 8)
print(fib(7)) #, 13)
print(fib(8)) #, 21)
print(fib(9)) #, 34)
print(fib(10)) #, 55)
print(fib(11)) #, 89)
print(fib(12)) #, 144)
print(fib(13)) #, 233)

"""def fib(n):
	a, b = 0, 1
	for x in range(n):
		a, b = b, a + b
	return a"""

"""def fibFast(n):
	s = 5**0.5
	P = (1 + s)/2
	p = (1 - s)/2
	return round((P**n - p**n) / s)"""
    
    
    


