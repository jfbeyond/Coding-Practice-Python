
# 204 Count Primes

# Use The Sieve of Eratosthenes approach
# just track numbers up until sqrt(n)

def countPrimes(n):

	if n < 2:
		return 0
		
	count = [1]*n
	count[0], count[1] = 0,0
	
	for i in range(2, int(n**0.5)+1):
		if count[i] == 1:
		
			count[i**2:n:i] = [0]*(int((n-1-i*i)//i)+1)
			
	return sum(count)
	
# O(n**2) and O(n)