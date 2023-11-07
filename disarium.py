"""A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.
Examples

is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True"""

def is_disarium(n):
    n = str(n)
    disList = []

    for i in n:
        disList.append(int(i))
    
    total = 0
    power = 1
    for number in disList:
        total += number ** power
        power += 1
        
    return True if total == int(n) else False

print(is_disarium(544))
print(is_disarium(518))
print(is_disarium(466))
print(is_disarium(8))

"""def is_disarium(n):
		return sum(int(i)**idx for idx, i in enumerate(str(n), 1)) == n"""
   


