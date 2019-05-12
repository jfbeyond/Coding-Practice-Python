

# 712 Min ASCII delete sum for two strings

# DP problem. I'll create a matrix to store the cost of deletion from bottom-up

def minimumDeleteSum(s1,s2):

        dp = [[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]


        # cost of single chars. from string 1
        for i in range(1,len(s1)+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        # cost of single chars. from string 2
        for i in range(1,len(s2)+1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])

        # Now populate the DP matrix

        for i in range(1, len(s1)+1):

            for j in range(1, len(s2) + 1):

                # If chars are equal store previous value
                if s1[i-1] == s2[j-1]:

                    dp[i][j] = dp[i-1][j-1]

                else:

                    # select minimum of either deleting char. from str 1 or from str2
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

        return dp[-1][-1]
		
	