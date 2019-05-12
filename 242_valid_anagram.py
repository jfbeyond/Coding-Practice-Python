
# 242 Valid Anagram

# Using hash table

def isAnagram(s,t)

	if len(s) != len(t): return False
	
	# make two dicts
	
	sdict = collections.defaultdict(int)
	tdict = collections.defaultdict(int)
	
	for ch in s: sdict[ch] += 1
	for ch in t: tdict[ch] += 1
	
	return sdict == tdict
	
# O(n) O(n)
	
# Using sorting  -- This doesn't work with unicode chars

def isAnagram(s,t):

	if len(s) != len(t): return False
	
	return s.sort() == t.sort()
	
# O(nlogn) O(1)