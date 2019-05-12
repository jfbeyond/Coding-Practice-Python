
# 88 Merge Sorted Array

# m and n are the numbers of initialized elements in both lists respectively
# nums1 has a total lenght of m+n 

def merge(nums1, m ,nums2,n):

	
	# as both arrays are sorted I can compare the biggest elements in each and the
	# greater goes towards the last available position. Then reduce corresponding index
	while m>0 and n>0:
	
		if nums1[m-1] >= nums2[n-1]:
			nums1[m+n-1] = nums1[m-1]
			m -= 1
		else:
			nums1[m+n-1] = nums2[n-1]
			n -= 1
	
	# if after terminating the loop n is still greater than zero, that means that nums2 has small numbers
	# that were not sorted and need to be appended at the beginning of the array.
	
	if n >0:
		nums1[:n] = nums2[:n]
		
	return nums1
	
# O(m+n) O(1)