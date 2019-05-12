

# 104 Max depth of Binary Tree

# Recursively

def maxDepth(root):

	if not root:
		return 0
		
	left = maxDepth(root.left)
	right = maxDepth(root.right)
	
	return 1 + left + right
	
# O(2**n) 0(1)


# Iteratively

def maxDepth(root):

	if not root:
		return 0
		
	queue = [root]
	h = 0
	
	while queue:
	
		lsize = len(queue)
		level = []
		
		for _ in range(lsize):
			node = stack.pop(0)
			level.append(node.val)
			if node.left:
				queue += [node.left]
			if node.right:
				queue += [node.right]
		h += 1
		
	return h
	
# O(n) O(1)