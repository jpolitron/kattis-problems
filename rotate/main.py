def rotate_array(input_array,k):
	k = k% len(input_array)
	for i in range(k):
		input_array.insert(0,input_array.pop(-1))
rotate_array([1,2,3,4,5,6,7],3)

