# Create a function that takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num. If 
# there are two numbers equidistant from num and divisible by n, select the larger one.
# Examples

# round_number(33, 25) ➞ 25

# round_number(46, 7) ➞ 49

# round_number(133, 14) ➞ 140

def round_number(num, n):
    r = [num//n * n, (num//n + 1) * n]
    return r[0] if num - r[0] < r[1] - num else r[1]

# print(round_number(33, 25)) # ➞ 25
# print(round_number(46, 7)) # ➞ 49
# print(round_number(133, 14)) # ➞ 140

print(round_number(34, 25)) #, 25)
print(round_number(54, 8)) #, 56)
print(round_number(65, 10)) #, 70)
print(round_number(6247, 163)) #, 6194)
print(round_number(532, 12)) #, 528)
print(round_number(642234, 1523)) #, 642706)
print(round_number(5123, 10)) #, 5120)
print(round_number(96623443, 7650)) #, 96627150)
print(round_number(125123, 520)) #, 125320)
print(round_number(12121212, 144)) #, 12121200)