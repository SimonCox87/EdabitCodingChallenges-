# The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero whose fact is 
# exactly divided by the number.

# kempner(6) ➞ 3

# 1! = 1 % 6 > 0
# 2! = 2 % 6 > 0
# 3! = 6 % 6 === 0

# kempner(10) ➞ 5

# 1! = 1 % 10 > 0
# 2! = 2 % 10 > 0
# 3! = 6 % 10 > 0
# 4! = 24 % 10 > 0
# 5! = 120 % 10 === 0

# A Kempner Function applied to a prime will always return the prime itself.

# kempner(2) ➞ 2
# kempner(5) ➞ 5

# Given an integer n, implement a Kempner Function.
# Examples

# kempner(6) ➞ 3

# kempner(10) ➞ 5

# kempner(2) ➞ 2

# Notes

#     Try solving this recursively, with an approach oriented to higher-order functions.
def fact(n):
    return n * fact(n-1) if n != 1 else 1

def kempner(k):
    f= [fact(i) % k for i in range(1,21)]
    return k if 0 not in f else f.index(0) + 1

# print(kempner(6)) # ➞ 3
# print(kempner(10)) # ➞ 5
# print(kempner(2)) # ➞ 2
# print(fact(13))

print(kempner(6)) #, 3, "Instructions: first example.")
print(kempner(10)) #, 5, "Instructions: second example.")
print(kempner(2)) #, 2, "Instructions: third example")
print(kempner(21)) #, 7)
print(kempner(1)) #, 1)
print(kempner(4)) #, 4)
print(kempner(13)) #, 13)
print(kempner(29)) #, 29)
print(kempner(68)) #, 17)
print(kempner(71)) #, 71)
print(kempner(100)) #, 10)

# def kempner(n, i=1, total=1):
#     return max(1, i-1) if total%n == 0 else kempner(n, i+1, total*i)





        


