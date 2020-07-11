def first_missing_positive_integer(integers):

	found_integers = []
	for integer in integers:
		if integer < 0:
			continue
		if integer + 1 > len(found_integers):
			extend_size = integer - len(found_integers) + 1
			found_integers.extend([False] * extend_size)
		found_integers[integer] = True

	missing_integer = 0
	for position in range(1,len(found_integers)):
		if found_integers[position] == False:
			missing_integer = position
			return missing_integer
	if missing_integer == 0 and len(found_integers) == 0:
		return 1
	elif missing_integer == 0 and len(found_integers) > 0:
		return len(found_integers)
print(first_missing_positive_integer([3, 4, -1, 1]))
