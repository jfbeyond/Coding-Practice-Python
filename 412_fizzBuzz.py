

# 412 Fizz Buzz

def fizzBuzz(n):

	output = []
	
	for i in range(1, n+1):
	
		if i % 3 == 0 and i%5 == 0:
			output += ["FizzBuzz"]
		elif i%3 == 0:
			output += ["Fizz"]
		elif i%5 == 0:
			output += ["Buzz"]
		else:
			output += [str(i)]
			
	return output
	
# O(n) and O(n)