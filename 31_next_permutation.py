

# 31 Next Permutation

def nextPermutation(nums):

	i = len(nums) - 1
	
	# Find largest index i such that nums[i-1] < nums[i]
	while i>0 and nums[i-1] >= nums[i]:
	
		i -= 1
		
	# if not i then it's already the greatest permutation. sort it
	if i<=0:
		return nums.sort()
		
	j = len(nums) - 1
	
	# Find pivot (j) such that j>=i and array[j] > array[i-1]
	while nums[j] <= nums[i-1]:
		j -= 1
		
	# swap pivot with element before index i
	nums[i-1],nums[j] = nums[j],nums[i-1]
	
	# reverse array after index i
	nums[i:] = nums[len(nums)-1:i-1:-1]
	
	return nums
	
# O(n), O(1)
		