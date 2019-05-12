
# 69 sqrt(x)
# Find the integer part of the square root of x

# Brute Force approach

def mySqrt(x):

	if x <= 3:
		return 1
		
	root = 2
	
	
	while root*root < x:
		
		root += 1
		
	return root if root**2 == x else root - 1
	
# O(x) O(1)



# Binary Search

def mySqrt(x):

	lo, hi = 0, x
	
	while lo <= hi:
	
		mid = (lo+hi)//2
		
		if mid**2 <= x:
			lo = mid + 1
		else:
			hi = mid - 1
			
	return lo-1
	
# O(log(x)) O(1)

