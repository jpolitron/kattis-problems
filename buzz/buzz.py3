x, y, n = input().split()
x = int(x)
y = int(y)
n = int(n)
for number in range(1,n+1):
    if number % x == 0 and number % y == 0:
      print("FizzBuzz"),
    elif number % x == 0:
      print("Fizz")
    elif number % y == 0:
      print("Buzz")
    else:
      print(number)
#translate into c++ and understand it

