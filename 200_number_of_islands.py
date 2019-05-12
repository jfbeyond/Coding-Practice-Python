
# 200 Number of islands - Graph problem


# Recursively

def numIslands(grid):

	islands = 0
	
	# Traverse grid and evaluate with DFS each node
	
	for i in range(len(grid)):
		for j in range(len(grid[0])):
		
			if grid[i][j] == 1:
				
				islands += 1
				dfscheck(grid,i,j)
				
	return inslands
	
def dfscheck(grid, i, j):

	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
	
		# Do nothing and return
		return
		
	grid[i][j] = "v"
	dfscheck(grid, i+1,j)
	dfscheck(grid, i-1,j)
	dfscheck(grid, i,j-1)
	dfscheck(grid, i,j+1)
	
	
	
# Iteratively

def numIslands(grid):

	islands = 0
	
	# Traverse grid and evaluate with DFS each node
	
	for i in range(len(grid)):
		for j in range(len(grid[0])):
		
			if grid[i][j] == 1:
				
				islands += 1
				
				for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
				
					
				dfscheck(grid,i,j)
				
	return inslands
	
def dfscheck(grid, i, j):

	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
	
		# Do nothing and return
		return
		
	grid[i][j] = "v"
	dfscheck(grid, i+1,j)
	dfscheck(grid, i-1,j)
	dfscheck(grid, i,j-1)
	dfscheck(grid, i,j+1)
