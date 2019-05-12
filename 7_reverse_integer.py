
# 7 Reverse Integer

def revInteger(n):

	if x < 0:
		sign = -1
		x *= sign
	else:
		sign = 1
		
	return sign*int(str(x)[::-1) if -2**31 <= x <= 2**31 - 1 else 0
	
# O(len(str(n)) --> O(1)  and O(1)