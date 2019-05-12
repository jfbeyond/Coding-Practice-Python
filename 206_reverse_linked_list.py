
# 206 Reverse Linked List

# Iteratively

def reverseList(head):

	if not head: return None
	
	prev = None
	current = head
	
	while current:
	
		temp = current.next
		current.next = prev
		prev = current
		current = temp
		
	return prev
	
# O(n) and O(1)


# Recursively

def reverseList(head , prev = None):

	if not head: return prev
	
	nextnode = head.next
	head.next = prev
	return reverseList(nextnode, head)

	
# O(n) and O(1)