def lastFactorial(x):
	result = x
	for i in range(1,x):
		result *= 1 * (x - i)
	last = str(result)
	print(last[-1:])
lastFactorial(1)
lastFactorial(2)
lastFactorial(100)

