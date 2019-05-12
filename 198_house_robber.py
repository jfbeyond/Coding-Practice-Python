
# 198 House Robber

# DP - Create array in which each cell stores the max that can be robbed up to house 'i'.
# First house - max equal to first house value
# second house - max of first two houses
# nth house - max of previous house or max of two houses before + current house value

def rob(nums):

	dp = [0]*(lens(nums)-1)
	dp[0] = nums[0]
	dp[1] = max(nums[:2])
	
	for i in range(2, len(nums)):
	
		dp[i] = max(dp[i-1], dp[i-2] + nums[i])
		
	return dp[-1]
	
# O(n) and O(n)

