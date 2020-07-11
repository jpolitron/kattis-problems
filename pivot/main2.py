def pivot(input_list):
	start = 0
	end = len(input_list)-1
	minimum = 0
	while start < end-1:
		if end - start % 2 == 0:
			pivot = int((end - start)/2) + start
		else:
			pivot = int((end - start + 1) /2) + start

		if input_list[pivot] < input_list[minimum]:
			end = pivot 
			minimum = pivot
		else:
			start = pivot
	return minimum
print(pivot([7,8,9,10,11,12,0,1,2,3,4,5,6]))
