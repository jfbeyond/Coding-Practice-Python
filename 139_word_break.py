

# 139 Word Break

# I'll track the words by using an array of same length as input
# that stores '1' at the end of the word if word exists in the dictionary

def wordBreak(s, worddict):

	dp = [0]*len(s)
	
	for i in range(len(s)):
	
		for word in worddict:
			
			# word checked since last char. backwards exists and its first index is 1 or -1.
			if word == s[i-len(word)+1:i+1] and (dp[i-len(word)] == 1 or i-len(word) == -1):
			
				dp[i] = 1
				
	return True if dp[-1] == 1 else False
	
	
	
# Alternative DP solution, slightly different, more elegant

def wordBreak(s, worddict):

	dp = [False]*(leng(s)+1)
	dp[0] = True
	
	for i in range(len(s)):
		for j in range(i, len(s)):
		
			if dp[i] and s[i:j+1] in worddict:
			
				dp[j+1] = True
				
	return dp[len(s)]