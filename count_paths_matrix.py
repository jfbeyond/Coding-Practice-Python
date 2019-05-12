

# Number of ways in matrix

# Find number of ways to go to the bottom-right corner from the origin

# Use of DP to acumulate the number of ways from bottom-up

def countPaths(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    
    nways = [[0 for i in range(cols)] for i in range(rows)]
    
    # base cases
    for i in range(rows):
        nways[i][0] = 1
    
    for i in range(cols):
        nways[0][i] = 1
    
        
    for i in range(1, rows):
        
        
        for j in range(1, cols):
        
            nways[i][j] = nways[i][j-1] + nways[i-1][j]
            
    
    return nways[-1][-1]
	
# O(n^2) O(n)
	