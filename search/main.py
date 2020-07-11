def search_for_range(array, target):
	location = []	
	if target in array:
		for i in range(len(array)):
			if array[i] == target:
				location.append(i)
			else:
				continue
		if len(location) == 1:
			location.append(array[0]-1)
			return location

	return [-1,-1]
	
print(search_for_range([5,7,7,8,8,10],8))
print(search_for_range([1],1))
