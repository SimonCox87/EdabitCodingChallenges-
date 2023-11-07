"""Write a function that takes a number and returns True if it's a prime; False otherwise. The number can be 2^64-1 (2 to the power of 
63, not XOR). With the standard technique it would be O(2^64-1), which is much too large for the 10 second time limit imposed by Edabit.

Examples

prime(7) ➞ True

prime(56963) ➞ True

prime(5151512515524) ➞ False"""

"""def prime(x):
    prime = True
    for i in range(2,(x // 2 ) + 1):
        if x % i == 0:
            prime = False
            break
    
    return prime"""

def prime(n):
    if n <= 1:          # negative numbers, 0 or 1
        return False
    if n <= 3:          # 2 and 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

print(prime(7)) #True
print(prime(5)) #True
print(prime(12)) #False
print(prime(777771)) #False
print(prime(207971)) #True
print(prime(100000074281)) #True
print(prime(100000074282)) #False
print(prime(777777777777777)) #False



"""def prime(x):
    return x > 1 and all(x % i for i in range(2, (x // 2) + 1))

print(prime(7)) #True
print(prime(5)) #True
print(prime(12)) #False
print(prime(777771)) #False
print(prime(207971)) #True
print(prime(100000074281)) #True
print(prime(100000074282)) #False
print(prime(777777777777777)) #False"""

