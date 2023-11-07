# You are given a list of prime factors lst and a target. When each number in the list is raised to an appropriate power their 
# product will be equal to the target.

# Your role is to return the exponents. All these lists will have a length of three. Basically, it is three numbers whose product 
# is equal to challenge. The only difference is what you are expected to return.

# Examples

# product_equal_target([2, 3, 5], 600) ➞ [3, 1, 2]
# # Because 2^3*3^1*5^2 = 600

# product_equal_target([2, 3, 5], 720) ➞ [4, 2, 1]
# # Because 2^4*3^2*5^1 = 720

# Notes

#     The exponents you will return are expected to replace the base in the list.
#     Your returned values must be in the same order as the bases.


def product_equal_target(lst, target):
    exps = []
    for i in lst:
        ex = 0
        while not target%i:
            target /= i
            ex += 1
        exps.append(ex)
    return exps

print(product_equal_target([2, 3, 5], 600)) # ➞ [3, 1, 2]
# Because 2^3*3^1*5^2 = 600
print(product_equal_target([2, 3, 5], 720)) # ➞ [4, 2, 1]
# Because 2^4*3^2*5^1 = 720