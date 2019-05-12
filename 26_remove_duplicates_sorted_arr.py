

# 26 Remove duplicates from sorted Array

# Do it in place, return the new length
# Use a check that represents a distinct number and gets updated everytime 
# a new number is found. 

def removeDuplicates(nums):

	c = 0
	check = nums[0]
	
	for i in range(1, len(nums)):
	
		if nums[i] != check:
		
			c += 1
			nums[c]= check
			check = nums[c]
			
	return c+1
	
# O(n) O(1)