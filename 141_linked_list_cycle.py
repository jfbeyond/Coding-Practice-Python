
# 141 Linked List Cycle

def hasCycle(head):

	if not head or not head.next:
		return False
		
	fast = slow = head
	
	while fast and fast.next:
	
		fast = fast.next.next
		slow = slow.next
		
		if fast == slow:
			return True
			
	return False
	
# O(n) O(1)

