
# Merge Intervals


def merge(intervals):

	result = []

	# Sort the array by start of intervals
	intervals.sort()

	for inter in intervals:

		# if interval start is less than end of previous result interval,
		# merge them
		if result and inter[0] <= result[-1][1]:
			result[-1][1] = max(inter[1], result[-1][1])

		# If not just append the interval to the results
		else:
			result.append(inter)

	return result