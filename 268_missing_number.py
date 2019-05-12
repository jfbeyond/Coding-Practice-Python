

# 268 Missing Number

# Find missing number in array that has n distinct numbers from 0 to n 

# Bit manipulation

def missingNumber(nums):

	res = 0
	
	for i in range(n):
		res ^= i
		
	for num in nums:
		res ^= num
		
	return res
	
# O(n) O(1)


# Math

def missingNumber(nums):

	currentSum = sum(nums)
	idealSum = len(sums)*(len(sums)+1)/2
	
	return idealSum - currentSum
	
# O(n) O(1)
		

	
