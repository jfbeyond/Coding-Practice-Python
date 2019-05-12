
# 189 Rotate Array

# Rotate to the right k steps


def rotate(nums, k):

	
	# if k > len of array then I'll just swap the extra positions
	k = k % len(nums)
	
	nums[:] = nums[-k:] + nums[:-k]
	
	return nums