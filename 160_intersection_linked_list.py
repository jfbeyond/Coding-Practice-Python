

# 160 Intersection of two linked lists

# Measure lenghts and shift pointer in longer list to reach starting pointer
# of shorter list

def intersection(headA, headB):

	if not headA or not headB: return None
	
	l1 = lenghtList(headA)
	l2 = lengthList(headB)
	dif = abs(l1-l2)
	
	# if list1 is bigger then shift its pointer
	if l1 >= l2:
		currentA = headA
		currentB = headB
		
		for _ in range(diff):
			currentA = currentA.next
		
	if l2 > l1:
		currentB = headB
		currentA = headA
		
		for _ in range(diff):
			currentB = currentB.next
			
	while currentA and currentB:
		if currentA == currentB:
			return currentA
		
		currentA = currentA.next
		currentB = currentB.next
		
	return None
	




def lenghtList(head):

	current = head
	c = 1
	
	while current:
		current = current.next
		c += 1
		
	return c
	
	
# O(n+m) O(1)