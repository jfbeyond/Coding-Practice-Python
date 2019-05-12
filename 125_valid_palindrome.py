

# 125 Valid Palindrome

def isPalindrome(s):

	news = [ch.lower() for ch in s if ch.isalnum()]
	
	return news == news[::-1]