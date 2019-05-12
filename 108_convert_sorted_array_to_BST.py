
# 108 Convert sorted Array to BST

# Assume you have a tree class to create nodes TreeNode()

def sortedArrayToBST(nums):

	if nums = []: return None
	
	# Auxiliar function to traverse array and make nodes
	def sortit(left, right):
	
		if left > right:
			return None
		mid = (left + right)//2
		node = TreeNode(nums[mid])
		node.left = sortit(left, mid)
		node.right = sortit(mid+1, right)
		
		return node
		
	return sortit(0, len(nums)-1)
	
# O(nlogn) and O(n)
	
	