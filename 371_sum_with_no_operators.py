
# 371 sum of integers without using addition or subtraction

def getSum(a,b):

	if a == -b:
		return 0
	if abs(a) > abs(b):
		a,b = b,a
	if a < 0:
		return -1*getSum(-a,-b)
	while b:
		c = a&b
		a ^= b
		b = c<<1
	return a
	
# O(32) , O(1)

		