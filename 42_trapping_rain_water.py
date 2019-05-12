
# 42 Trapping rain water

# Keep track of max before and after current element

def trap(height):

	if len(height) == 0: return 0
	
	maxBef = height[0]
	trapped = 0
		
	for i in range(1,len(height)):
		if height[i] > maxBef:
			maxAft = height[i]
			break
	
	for i in range(1, len(height)):
	
		if maxBef < height[i]:
			maxBef = height[i]
			
		if maxAft == height[i]:
			maxAft = max(height[i+1:])
			
		
		if maxBef > height[i] and maxAft > height[i]:
			trapped += min(maxAft, maxBef) - height[i]
			
	return trapped
	