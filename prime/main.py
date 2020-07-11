def isPrime(n):
	for currentNumber in range(2,n):
		if n % currentNumber == 0:
			return False
	return True
def countPrimes(n):
	count = 0
	for currentNumber in range(2,n):
		if isPrime(currentNumber) and currentNumber < n:
			count += 1
	print(count)
countPrimes(10)
countPrimes(20)
countPrimes(23)
countPrimes(30)
countPrimes(40)
