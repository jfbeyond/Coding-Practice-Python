
# 101 Symmetric Tree

# Recursively

def isSymmetric(root):

	# current node left child is equal to current node right child
	
	if not root: return False
	
	return checkSymmetry(root, root):
	
	
def checkSymmetry(node1, node2):

	if not node1 and not node2: return True
	
	if node1 and node2 and node1.val == node2.val:
	
		return checkSymmetry(node1.left, node2.right) and checkSymmetry(node1.right, node2.left)
		
	return False

	
# O(n) and O(1)


# Iteratively

def isSymmetric(root):

	# BFS -- Queue
	
	stackl = [root]
	stackr = [root]
	
	while stackl and stackr:
	
		nl = stackl.pop(0)
		nr = stackr.pop(0)
		
		# if both nodes are none just go to next iteration
		if not nl and not nr:
			continue
		# This means only one is None, then it's False
		if not nl or not nr:
			return False
		if nl.val != n2.val:
			return False
		stackl.append(nl.left)
		stackl.append(nl.right)
		stackr.append(nr.right)
		stackr.append(nr.left)
		
	return True
	
# O(n) and O(n)