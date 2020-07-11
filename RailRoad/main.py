'''
Puesdo:
1. take in x and y.
2. check if y mod 2 == 0 if so print possible.
3. else print impossible
'''
x,y = map(int,input().split())
if y % 2 == 0:
    print("possible")
else:
    print("impossible")
