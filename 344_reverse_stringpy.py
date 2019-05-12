
# 344 Reverse string in place

def reverseString(string):

	for i in range(len(string)):
	
		string[i], string[len(string)-1-i] = string[len(string)-1-i], string[i]
		
	return
	
# O(n) and O(1)
