"""Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:
Examples

fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200"""

def fact_of_fact(n):
    fLst = []
    pre = 1
    for i in range(1, n + 1):
        fLst.append(i * pre)
        pre = i * pre
    
    fact = 1
    for i in fLst:
        fact *= i
    return fact

print(fact_of_fact(4))
print(fact_of_fact(5))
print(fact_of_fact(6))

from math import factorial, prod

def fact_of_fact(n):
    fact = [factorial(i) for i in range(1, n + 1)]
    return prod(fact)

print(fact_of_fact(4))
print(fact_of_fact(5))
print(fact_of_fact(6))