
# 14 longest common prefix

def longestCommonPrefix(strs):

    if strs == [] or strs[0] == "": return ""

    if len(strs) == 1: return strs[0]

    minlen = min(len(s) for s in strs)

    prefix = ""

	for i in range(minlen):
		ch = strs[0][i]
		for s in strs:
			if ch != s[i]:
				return prefix
		prefix += ch

	return prefix
			
# O(n*minlen) O(1)
	
		
		
			

