
# 38 Count and Say


def countAndSay(n):

	results = ["1", "11"] + [""]*(n-2)
	
	# Go through each one of the strings until you reach n row
	for i in range(1, n):
		
		# will start as first number of previous string
		pointer = results[i-1][0]
		c = 1
		
		# Go through each one of the remaining numbers in the current string
		for j in range(1, len(results[i-1])):
		
			# if current number is equal to pointer then count it
			if results[j-1] == pointer:
				c += 1
			# if not then store its count and value in current string
			else:
				results[i] += str(c) + str(pointer)
				pointer = results[j-1]
				c = 1
		
			# Store any remaining count and pointer from the last pass
			if j == len(results[i-1]) - 1:
				results[i] += str(c) + str(pointer)
		
	return results[-1]
				