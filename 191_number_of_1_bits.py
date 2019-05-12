
# 191 Number of 1 bits

def hammingWeight(n):

	# Bit manipulation
	# when I bit 'and' a number with its previous number I'm eliminating a '1' in its binary representation
	
	c = 0
	while n:
		n ^= n-1
		c += 1
		
	return c
	
# O(32) and O(1)	

# Pythonic
	
def hammingWeight(n):

	return format(n,'b').count(1)
	
# O(32) and O(1)	