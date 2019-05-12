
# 53 Max. Subarray

# Find it but return its sum, not the array
# Kadane's algorithm

# can have negative numbers

def maxSubArray(nums):

	if len(nums) == 1: return nums[0]
	
	max_so_far = float('-inf')
	max_here = float('-inf')
	
	for num in nums:
	
		max_here = max(num, max_here + num)
		max_so_far = max(max_so_far, max_here)
		
	return max_so_far
		
	
	
	