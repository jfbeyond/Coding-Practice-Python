

# 234 Palindrome Linked List
# Do it in linear time and constant space
# Find the middle of the list with two pointers and then reverse the second half
# and compare with the first half

def isPalindrome(head):

	if not head and (head and not head.next): 
		return True
	
	# Find middle node
	middle = head
	fast = head
	
	while fast and fast.next:
	
		fast = fast.next.next
		middle = middle.next
		
	
	# Reverse second half
	prev = None
	
	while middle:
	
		temp = middle.next
		middle.next = prev
		prev = middle
		middle = temp
		
	
	# Compare first and second half

	while prev:
	
		if prev.val != head.val:
			return False
			
		prev = prev.next
		head = head.next
		
	return True
	
# O(n) O(1)
	

