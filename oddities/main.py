'''
Puesdo:
1. take the number from user.
2. check if even or odd.
3 .print the message
'''
import math
cases = int(input())
x = 0
for i in range(cases):
    x = int(input())
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
