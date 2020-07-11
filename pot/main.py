'''
Puesdo:
1. take in the number of cases.
2. take in each number using a for loop.
3. seprate the number with the power.
4. calculate and add to total.
5. return value.
'''
import math
cases = int(input())
x = 0
for i in range(0, cases):
    num = int(input())
    base = num //10
    power = num%10
    x += base ** power
print(x)
