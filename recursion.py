# Create a function that filters out factorials from a list. A factorial is a number that can be represented in the following manner:

# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

# Recursively, this can be represented as:

# n! = n * (n-1)!

# Examples

# filter_factorials([1, 2, 3, 4, 5, 6, 7]) ➞ [1, 2, 6]

# filter_factorials([1, 4, 120]) ➞ [1, 120]

# filter_factorials([8, 9, 10]) ➞ []

# def filter_factorials(numbers):
#     n = [i for i in numbers]
#     facts = []
#     for i in n:
#         div = 1
#         while i and i != 1:
#             i /= div
#             if i%1:
#                 break
#             div += 1
#         facts.append(i)
    
#     return [numbers[i] for i in range(len(facts)) if not facts[i]%1]

def factorial(n):   
    return n * factorial(n-1) if n != 1 else 1

def filter_factorials(number):
    return list(filter(lambda x : x in [factorial(i) for i in range(1,21)], number))

print(factorial(4))
print(filter_factorials([1, 2, 3, 4, 5, 6, 7])) # ➞ [1, 2, 6]
print(filter_factorials([1, 4, 120])) # ➞ [1, 120]
print(filter_factorials([8, 9, 10])) # ➞ []
