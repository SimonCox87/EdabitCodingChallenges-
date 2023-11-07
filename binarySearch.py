"""Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your function. 
The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".
Examples

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


is_prime(primes, 3) ➞ "yes"

is_prime(primes, 4) ➞ "no"

is_prime(primes, 67) ➞ "yes"

is_prime(primes, 36) ➞ "no"

24, 12, 6, 3, 2, 1
Notes

    You could use built-in functions to solve this, but the point of this challenge is to see if you understand the binary search algorithm.
    The solution is in the Resources tab."""

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def is_prime(primes, num, left=0, right=None):
    right = len(primes) - 1
    guess = primes[right - left // 2]
    
    while guess != num and left < right:
        if guess < num:
            left = primes.index(guess) + 1
            guess = primes[right - left // 2]
        if guess > num:
            right = primes.index(guess) - 1
            guess = primes[right - left // 2]
    
    return "yes" if guess == num else "no"
        
print(is_prime(primes, 3)) # ➞ "yes"
print(is_prime(primes, 4)) # ➞ "no"""
print(is_prime(primes, 67)) # ➞ "yes"
print(is_prime(primes, 36)) # ➞ "no"

"""def is_prime(primes, num):
	lo = 0
	hi = len(primes)
	while hi-lo>1:
		h = (hi+lo)//2
		if num >= primes[h]:
			lo = h
		else:
			hi = h
	return 'yes' if primes[lo]==num else 'no'"""

