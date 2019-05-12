



# 516 Longest Palindromic Subsequence

def LPSstring(st):

	if st == st[::-1]:
		return len(st)
	
	dp = [[0]*len(st) for _ in range(len(st))]


	for i in range(1,len(st)):

		for j in range(len(st)-1,-1,-1):

			# Base case, more than half of the array has been traversed
			if j > i:
				dp[j][i] = 0
			# Base case, the indexes are in the middle char, which is a palindrome
			elif i==j:
				dp[j][i]= 1
			else:

				if st[j] == st[i]:
					dp[j][i] = 2+dp[j+1][i-1]
				else:
					dp[j][i] = max(dp[j][i-1], dp[j+1][i])

	
	return dp[0][-1]

	
# O(n^2) O(n^2)