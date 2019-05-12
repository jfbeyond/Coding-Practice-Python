

# 350 Intersection of two arrays

def intersect(nums1, nums2):

	numdict = collections.defaultdict(int)
	ans = []

	for num in nums1:
		numdict[num] += 1

	for num in nums2:
		if num in numdict and numdict[num] > 0:
			numdict[num] -= 1
			ans += [num]

	return ans
	
	
# 349 Intersection of two arrays - Result unique

def intersection(nums1, nums2):

	l1 = len(nums1)
	l2 = len(nums2)
	numdict = collections.defaultdict(int)

	if l1 >= l2:
		for num in nums2:
			numdict[num] += 1
		nums = nums1	
	else:
		for num in nums1:
			numdict[num] += 1
		nums = nums2

	ans = []

	for num in nums:
		if num in numdict and num not in ans:
			ans += [num]
	return ans
		
# O(n+m)  O(n)
			

