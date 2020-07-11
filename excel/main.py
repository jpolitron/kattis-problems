def excel(letter):
	result = 0
	for i in range(0, len(letter)):
		result *= 26
		print(ord(letter[i]));
		result += (ord(letter[i]) - ord('A') + 1)
	return result
print(excel("BB"))
