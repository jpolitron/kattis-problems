def matrix_search(matrix, target) -> bool:
	flag = 0
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == target:
				flag = 1
			else:
				continue
	return flag
print(matrix_search([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
