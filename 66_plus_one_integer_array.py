

# 66 Plus one

# input --> [4,3,2,1]
# output --> [4,3,2,2]

# Using python conversions

def plusOne(digits):

    if digits[0] == 0:
        return 1
    
    digits = [str(d) for d in digits]
    
    nums = str(int(''.join(digits)) + 1)
    
    num = [int(n) for n in nums]
    
    return num
	
# O(n) O(n)
	

# Using math

def plusOne(digits):

	number = 0
	
	for i in range(len(digits)):
	
		number += digits[i]*10**(len(digits)-1-i)
		
	number += 1
	
	output = []
	
	while number>0
	
		digit = number % 10
		number = number//10
		output += [digit]
		
	return output
	
# O(n) O(1)