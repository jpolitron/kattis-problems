'''
Puesdo:
1. take in x's and y's.
2. then pass through function
3. have it check if the first and second are the same if so return 3rd.
4. have it check 2nd and 3rd then return 1st
5. all fails return the second
'''
for i in range(2):
    a,b,c = map(int,input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    else:
        print(b)
