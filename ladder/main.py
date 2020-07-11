'''
1. take in height and v degrees
2. calculate the length
3. print out the result
'''
import math
height, degree = map(int,input().split())
result = (height/math.sin(math.radians(degree)))
print(math.ceil(result))
