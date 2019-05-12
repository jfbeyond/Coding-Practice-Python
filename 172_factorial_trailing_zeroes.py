

# 172 Factorial trailing zeroes

# The number of trailing zeroes depends on if the number can be divided by 5, 25, 125, etc.
# each one adding one trailing zero (5 - 0, 25 -00, 125 - 000)

def trailingZeroes(n):

	c = 0
	
	while n>0:
	
		n /= 5
		c += n 
		
	return c

	# O(log(n)) O(1)
