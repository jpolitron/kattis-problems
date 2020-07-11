'''
Puesdo:
1. take in a,b in input split.
2. reverse the the numbers.
3 compare th largest.
4. print out the biggest
'''
a,b = map(str,input().split())
a = a[::-1]
b = b[::-1]

if int(a) < int(b):
    print(b)
else:
    print(a)
