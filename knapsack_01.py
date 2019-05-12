



def knapsack(p,w,c):

    dp = [[0 for _ in range(c+1)] for _ in range(len(p)+1)]
    
    
    for i in range(1, len(p)+1):
        
        for j in range(1, c + 1):
        
            # If current item weight greater than current capacity, don't include item
            if w[i-1] > j:
                dp[i][j] = dp[i-1][j]   #current max. is equal to previous current max
            # if it's less then include it and take the maximum between having it or not having it
            else:    
                dp[i][j] = max(dp[i-1][j], p[i-1] + dp[i-1][j-w[i-1]])
                
    print(dp)            
    return dp[-1][-1]
    
p = [100,20,60,40]
w = [3,2,4,1]
c = 5

print(knapsack(p,w,c))
