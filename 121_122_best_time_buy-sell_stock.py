

# 121 Best Time to buy and sell stock

# DP problem, Bottom-up

def maximumProfit(prices):
	
	if len(prices) == 0 or len(prices) == 1:
		return 0
	
	minPrice = prices[0]
	maxProfit = 0
	
	for i in range(1, len(prices)):
	
		maxProfit = max(maxProfit, prices[i] - minPrice)
		minPrice = min(minPrice, prices[i])
		
	return maxProfit
	
	
# O(n) time and O(1) space


# 122 Best Time to buy and sell stock if I can have multiple transactions

def maximumProfit(prices):

	
	if len(prices) == 0  or len(prices) == 1:
		return 0
		
	profit = 0
	
	for i in range(len(prices)-1):
	
		# If price of next day is greater than current's then sell and store profit
		if prices[i+1] > prices[i]:
			
			profit += prices[i+1] - prices[i]
			
	return profit 
	
	