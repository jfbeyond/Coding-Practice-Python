
# 190 Reverse Bits

def reverseBits(n):

	numbit = format(n,'b').zfill(32)
	return int(numbit[::-1],2)
	
# O(32) O(1)


	
	