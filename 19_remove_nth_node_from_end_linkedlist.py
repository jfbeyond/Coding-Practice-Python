

# 19 Remove Nth Node From end of linked list


def removeNthFromEnd(head, n):

	if not head: return None
	
	# Find pointer that starts n pos. after head
	c = 0
	pointer = head
	while c < n:
		pointer = pointer.next
		c += 1
		
	dummy = ListNode(None)
	dummy.next = head
	prev = dummy
	
	
	#prev = None
	#current = head
	
	while pointer:
		
		prev = current
		current = current.next
		pointer = pointer.next
		
	prev.next = current.next
	
	return dummy.next
	
# O(n) O(1)

	