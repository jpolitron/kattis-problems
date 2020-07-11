def power_of_three(n:int):
	flag = False
	if n == 0:
		return flag
	while n % 3 == 0:
		n = n//3
	if n == 1:
		flag = True
		return flag
	else:
		return flag
print(power_of_three(27))
print(power_of_three(0))
print(power_of_three(9))
print(power_of_three(45))
