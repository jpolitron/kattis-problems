def find_index(sorted_list, target):
	if target not in sorted_list:
		sorted_list.append(target)
		sorted_list.sort()
		return sorted_list.index(target)
	else:
		return sorted_list.index(target)
print(find_index([1,3,5,6],5))
print(find_index([1,3,5,6],2))
print(find_index([1,3,5,6],7))
print(find_index([1,3,5,6],0))
