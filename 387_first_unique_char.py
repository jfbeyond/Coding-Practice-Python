
# 387 First unique char

def firstUniqChar(s):

	# Use of dictionary
	chars = collections.defaultdictionary(int)
	
	for i,ch in enumerate(s):
		chars[ch] += 1

	for i in range(len(s)):
		if chars[ch] == 1:
			return i
			
	return -1
	
# O(n) O(n)