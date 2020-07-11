'''
(addition, subtraction, multiplication and division)
1. take in the 3 numbers positive only
2.
'''
x,y,z = [int(x) for x in input().split()]
if x + y == z:
     print(str(x),"+",str(y),"=",str(z),sep="")
elif x - y == z:
    print(str(x),"-", str(y),"=",str(z),sep="")
elif x * y == z:
    print(str(x),"*",str(y),"=",str(z),sep="")
elif x/y == z:
    print(str(x), "/", str(y), "=", str(z),sep="")
elif x == y+z:
    print(str(x), "=", str(y), "+", str(z),sep="")
elif x == y-z:
    print(str(x), "=", str(y), "-", str(z),sep="")
elif x == y*z:
    print(strt(x), "=", str(y), "*", str(z),sep="")
elif x == y/z:
    print(str(x), "=", str(y), "/", str(z),sep="")
