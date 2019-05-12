
# 50 Pow(x,n)

# Find x^n

# Bit manipulation

def myPow(x, n):

	# if n is negative just invert x and make n positive
	if n < 0:
		x = 1/x
		n = -n
		
	result = 1
	
	while n:
	
		if n & 1:
			result *= x 
		x *= x 
		n >>= 1
		
	return result