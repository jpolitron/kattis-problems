'''
Puesdo:
1. start from 1.
2. take in x,y,n using input split.
3. divisable by x fizz.
4. divisable by y buzz.
5. both fizz buzz.
'''
x,y,n = map(int,input().split())

for i in range(1,n+1):
    if i % x == 0 and i% y == 0:
        print("FizzBuzz")
    elif i % x == 0:
        print("Fizz")
    elif i % y == 0:
        print("Buzz")
    else:
        print(i)
