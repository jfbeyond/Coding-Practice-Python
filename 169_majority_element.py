

# 169 Majority Element

def majorityElement(nums):

	for num in nums:
	
		numdict[num] += 1
		if numdict[num] >= len(nums)/2:
			return num
			
#  O(n) and O(n)