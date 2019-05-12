
# 94 Binary Tree InOrder Traversal

# Recursively

def inOrder(root, ans = []):

	if not root:
		return []
		
	if root.left:
		inOrder(root.left)
		
	ans += [root.val]
	
	if root.right:
		inOrder(root.right)
		
	return ans
	
	
# O(2^n) O(1)


# Iteratively

def inOrder(root):

	# This is a bit more elaborate. A stack will be used in which nodes to te left of current
	# are stored first until null is found. Then a node is popped from stack and its value included in the
	# answer. And current node is now the right of the node.
	
	current = root
	ans = []
	stack = []
	
	while True:
	
		if current:
			stack += [current]
			current = current.left
		else:
			if len(stack)>0:
				current = stack.pop()
				ans += [current.val]
				current = current.right
			
			else:
				break
				
	return ans
	
# O(n) O(n)