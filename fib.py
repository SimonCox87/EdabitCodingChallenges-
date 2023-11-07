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

print(fibonacci1(1))