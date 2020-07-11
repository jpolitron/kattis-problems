def find_index(sorted_list, target):
	for i in range(len(sorted_list)):
		if sorted_list[i] == target:
			return i
		elif sorted_list[i] + 1 == target:
			sorted_list.insert(i+1,target)
			return sorted_list.index(target)
	return 0
print(find_index([1,3,5,6],5))
print(find_index([1,3,5,6],2))
print(find_index([1,3,5,6],7))
print(find_index([1,3,5,6],0))
print(find_index([1,3,5,9],3))
print(find_index([1,3,5,9],2))
print(find_index([1,3],2))
