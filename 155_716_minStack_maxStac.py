
# 155 Design a Stack that supports push, pop, top and retrieve of min element in constant time

class MinStack(object):

	def __init__(self):
	
		self.st = []
		self.minArray = [}
		
	def push(self, number):
	
		self.st.append(number)
		
		if len(self.st) == 0:
			self.minArray.append(number)
			
		if number <= self.minArray[-1]:
			self.minArray.append(number)
			
	def pop(self):
	
		last = self.st.pop()
		
		if last == self.minArray[-1]:
			self.minArray.pop()
			
	def top(self):
	
		return self.st[-1]
		
	def getMin(self):
	
		return self.minArray[-1]
		

# 716  Design a Max Stack. Have also a max pop function

class MaxStack(object):

	def __init__(self):
	
		self.st = []
		self.maxArray = []
		self.ind = 0
		
	def push(self, number):
	
		self.st.append(number)
		
		if len(self.maxArray) == 0:
			self.maxArray.append((number, self.ind))
			
		if number >= self.maxArray[-1]:
			self.maxArray.append((number, self.ind))
			
		self.ind += 1
			
	def pop(self):
	
		last = self.st.pop()
		
		if last == self.maxArray[-1][0]:
			self.maxArray.pop()
			
	def top(self):
	
		return self.st[-1]
		
	def getMax(self):
	
		return self.maxArray[-1]
		
	def popMax(self):
	
		lastMax, lastind = self.maxArray.pop()
		self.st.pop(lastind)
		
	
	
		
		
		