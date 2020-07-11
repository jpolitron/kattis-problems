import math

result = 0
number = int(input())
s = bin(number)
#removing "0b" prefix
s1 = s[2::]
reversed = s1[::-1]
print(int(reversed,2))
