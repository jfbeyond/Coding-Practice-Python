
# 20 Valid Parenthesis

def isValid(s):

	checkOpen = '([{'
	trackOpen = []
	combinations = [('(',')'), ('[',']'), ('{','}')]
	
	for par in s:
	
		if par in checkOpen:
		
			trackOpen += [par]
		
		else:
		
			if (trackOpen[-1], par) in combinations:
			
				trackOpen.pop()
			
			else:
				return False
				
	return True if trackOpen = [] else False