import math
def squareRoot(num):
	x = int(num ** 0.5)
	if int(x + 0.5) ** 2 == num:
		return x
	else:
		y = math.floor(x)
		return int(y)
print(squareRoot(11))
print(squareRoot(9))
print(squareRoot(1))

