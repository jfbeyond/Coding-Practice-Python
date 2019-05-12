
# 326 Power of three

# Find a function to determine if number is power of three

# X ^ 3 = num --> x = log3(num) --> x = log(num)/log(3)

def isPowerOfThree(num):

	return True if (log(num)/log(3)).is_integer() else False
	


# Alternative
# Find biggest number in Python being a power of 3. 
# This ceiling is 3**19

def isPowerOfThree(num):

	return True if n>0 and 3**19 % num == 0 else False
	