def pivot(input_list):
	for current in range(1,len(input_list)):
		if  input_list[current] > input_list[current-1]:
			return current
	return 0

print(pivot([0,1,2,4,5,6,7]))

