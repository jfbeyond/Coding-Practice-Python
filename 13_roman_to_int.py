
# 13 Roman to Integer

def romanToInt(s):

	romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	scases = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM": 900}

	ans, c = 0,0
	
	# tracking of letters in array from left to right
	while c < len(s):
	
		# if two chars are double romans and the char after is a single roman
		if len(s[c:]) > 2 and s[c:c+2] in scases and s[c+2] in romans:
			ans += scases[s[c:c+2]]
			c += 2
			continue

		# if last two chars are double romans
		if len(s[c:]) == 2 and s[c:] in scases:
			ans += scases[s[c:]]
			c += 2
			continue
			
		# if single char. is a roman
		if s[c:c+1] in romans:
			ans += romans[s[c:c+1]]
			c += 1
			
	return ans
	
# O(n) O(1)


# Alternative

def romanToInt(s):

	romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	
	s = s.replace("IV", "IIII").replace("IX","VIIII")
	s = s.replace("XL", "XXXX").replace("XC","LXXXX")
	s = s.replace("CD", "CCCC").replace("CM","DCCCC")
	
	res = 0
	
	for char in s:
	
		res += romans[char]
		
	return res