
# 283 Move zeroes
# In Place

def moveZeroes(nums):

	c = 0
	
	for i in range(len(nums)):
	
		if nums[i] != 0:
			nums[i], nums[c] = nums[c], nums[i]
			c += 1
			
	return nums

# O(n), O(1)