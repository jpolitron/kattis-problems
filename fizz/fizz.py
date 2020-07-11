def fizzbuzz(n):
	vals = []
	for i in range(1 ,n+1):
            if i % 3 == 0 and i % 5 == 0:
                vals.append("FizzBuzz")
            elif i % 3 == 0:
                vals.append("Fizz")
            elif i % 5 == 0:
                vals.append("Buzz")
            else:
                vals.append(i)
	print(vals)
fizzbuzz(7)



