# Create a function that finds how many prime numbers there are, up to the given integer.
# Examples

# prime_numbers(10) ➞ 4
# # 2, 3, 5 and 7

# prime_numbers(20) ➞ 8
# # 2, 3, 5, 7, 11, 13, 17 and 19

# prime_numbers(30) ➞ 10
# # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

def prime_numbers(num):
	return sum(1 for i in range(2,int(num)) if all(i%j for j in range(2,i)))

def prime_numbers(num):
	p = []
	c = 2
	while c <= num:
		flag = True

		for i in range(2,(c//2)+1):
			if not c%i:
				flag = False
				break
		
		if flag:
			p.append(c)
		c += 1
	
	return len(p)


print(prime_numbers(10)) # ➞ 4
# 2, 3, 5 and 7
print(prime_numbers(20)) # ➞ 8
# 2, 3, 5, 7, 11, 13, 17 and 19
print(prime_numbers(30)) # ➞ 10
# 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

# def prime_numbers(num):
# 	return sum(1 for i in range(2,int(num)) if all(i%j for j in range(2,i)))

# def prime_numbers(num):
# 	return sum(all(i%x for x in range(2,i)) for i in range(2,num))


