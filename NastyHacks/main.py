'''
Puesdo:
n -> cases
r -> not advertise
e -> do advertise
c -> cost

1. take in cases.
2. take in r,e, and c.
3. e - c == r :not matter
4. e - c > r : advertise
5. else dont advertise
'''
cases = int(input())
for i in range(cases):
    r,e,c = list(map(int,input().split()))
    if e-c == r:
        print("does not matter")
    elif e - c > r:
        print("advertise")
    else:
        print("do not advertise")
    del r,e,c
