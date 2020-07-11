import math
count = 0
n = math.factorial(int(input()))
lst = str(n)
i = len(lst)-1
while i >= 0:
    if lst[i] != '0':
        break
    else:
        count +=1
    i -=1
print(count)
