'''
1. take in l,d and x
2. create a list with the results
3. loop from l to d+1
4.have total that
'''
l, d, x = int(input()), int(input()), int(input())
result = []

for i in range(l, d+1): #loop from l to d+1
    total = 0
    str(i)
    for j in str(i):
        total += int(j)
    if total == x:
        result.append(int(i))
print(str(min(result)) + "\n" + str(max(result)))
