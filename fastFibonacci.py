"""n mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1:

Fibonacci Sequence

and

Fibonacci Sequence 2

for n > 1

The beginning of the sequence is thus:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

The function fib_fast(num) returns the fibonacci number Fn, of the given num as an argument.
Examples

fib_fast(5) ➞ 5

fib_fast(10) ➞ 55

fib_fast(20) ➞ 6765

fib_fast(50) ➞ 12586269025

Notes

    The input number is always positive.
    Edabit would fail your code if it's not Fast enough."""

import timeit
import time
def fib_fast(num):
    fibSeq = []
    f0, f1 = 0, 1
    for i in range(num + 1):
        if i >= 1:
            i = f0 + f1
        f0, f1 = f1, i
        fibSeq.append(i)

    return fibSeq[-1]

print(fib_fast(1000000))
test_code2 = """
fibonacci_cache = {}
def fibonacci1(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci1(n-1) + fibonacci1(n-2)
    
    fibonacci_cache[n] = value
    return value

for i in range(1000001):
    print(fibonacci1(i))"""

from functools import lru_cache
test_code3 = """
@lru_cache(maxsize=1001)
def fibonacci2(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci2(n-1) + fibonacci2(n-2)

    return value

for i in range(1000001):
    print(fibonacci2(i))"""

"""print(timeit.repeat(stmt="test_code1", number=1, globals=globals()))
print(timeit.repeat(stmt="test_code2", number=1, globals=globals()))
print(timeit.repeat(stmt="test_code3", setup="from functools import lru_cache", number=1, globals=globals()))"""

def fibFast(num):
    a, b = 0, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return b

def fibFast(n):
	s = 5**0.5
	P = (1 + s)/2
	p = (1 - s)/2
	return round((P**n - p**n) / s)
