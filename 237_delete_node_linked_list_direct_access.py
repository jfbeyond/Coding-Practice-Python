

# 237 Delete Node in Linked list except the tail (if we're given acces only to that node)

def deleteNode(node):

	node.val = node.next.val
	node.next = node.next.next
	
