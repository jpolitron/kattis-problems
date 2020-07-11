'''
Puesdo:
1. take in cases.
2. take in x,y.
3.create a loop from x to y+1
4. insert that index to the set.
5. print the length of the set.
'''
cases = int(input())
result = set()

for i in range(cases):
    x,y = map(int,input().split())
    for j in range(x,y+1):
        result.add(j)
print(len(result))
