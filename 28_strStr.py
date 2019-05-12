

# 28 Implement strStr()
# Return index of first ocurrence of string in string

def strStr(big, small):

	if small == []: return 0
	
	if small not in big:
		return -1
	else:
		for i in range(len(big)-len(small)+1):
		
			if big[i:i+len(small)] == small:
				return i
				
# O(n*m) O(1)