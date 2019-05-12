
# 171 Excel Column Number

def titleToNumber(s):

	# Conversion of base 26 to base 10
	# Find ascii number for letters 
	
	res = 0
	
	for ch in s:
	
		res = res*26 + ord(ch) - ord('A') + 1
		
	return res
	
# O(n) and O(1)


def converToTitle(n)

	alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
	
	res = ""
	
	while n > 0:
	
		index = (n-1) % 26
		result += alphabet[index]
		n = int((n-1)/26)
		
	return res
	
# O(n) and O(26)