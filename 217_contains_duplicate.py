
# 217 Contains duplicate

# Using hash table

def containsDuplicate(nums):

	numbers = {}
	
	for num in nums:
		if num not in numbers:
			numbers[num] = 1
		else:
			numbers[num] += 1
		if numbers[num] == 2:
			return True
			
	return False
		
# O(n) O(n)

# Alternative

def containsDuplicate(nums):

	distinct = list(set(nums))
	
	return len(nums) != len(disctinct)