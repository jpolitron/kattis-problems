def search_for_range(array, target):
	location = []
	low = 0
	high = len(array)-1
	if target in array:
		while low <= high:
			mid = (low + high) // 2
			if target == array[mid]:
				location.append(mid)
			elif target < array[mid]:
				high = mid - 1
			else:
				low = mid + 1
		return location
	return [-1,-1]



print(search_for_range([5,7,7,8,8,10],8))
print(search_for_range([1],1))
