'''
Puesdo:
1. take in the number of cases.
2. take in the numbers you want to do facotrial.
3. get the last digit of the factorial.
4. print the last digit.
'''
import math
cases = int(input())
for i in range(cases):
    x = int(input())
    print(math.factorial(x)%10)
