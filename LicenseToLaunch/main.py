'''
Puesdo:
1. take in cases.
2. take in space junk.
3. find the smallest
4. return that index
'''
cases = int(input())
x = list(map(int,input().split()))
location = x.index(min(x))
print(location)
