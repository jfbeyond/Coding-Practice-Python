
# 136 Single Number

# Find number that appears only once when all appear twice


# Bit manipulation problem. Use XOR

def singleNumber(nums):

	single = nums[0]
	
	for i in range(1,len(nums)):
	
		single ^= nums[i]
		
	return single
		
		
# O(n) and O(1)


# 137 Single number. Here numbers show up three times except one


def singleNumber(nums):

	result = [0]*32
	
	for num in nums:
		for i in range(32):
			bit = num>>i & 1
			result[i] += bit
			
	ans = 0
	for i in range(len(result)):
		if result[i] % 3 != 0:
			ans += 2**i
			
	return ans
	
# O(n) and O(1)