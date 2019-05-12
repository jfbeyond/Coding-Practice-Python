
# 202 Happy Number

# Use cycle idea. We move a fast pointer as twice the sumsquare of the number along with a slow
# one with once the sumsquare. When they meet the loop breaks. If they're equal to 1 then it's a happy
# number	

def isHappyNumber(n):

	
	def sumSq(n):
		sqsum = 0
		while n:
			sqsum += (n%10)**2
			n = n//10
		return sqsum

	fast = slow = n
	
	while True:
		slow = sumSq(n)
		fast = sumSq(sumSq(n))
		if slow == fast:
			break
			
	retun slow == 1
	
	
		