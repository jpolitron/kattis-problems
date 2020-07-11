'''
1. take in two numbers
2. check if the numbers are the same and greater than 0
3. if so print even with the sum
4.else print odd and check the smallest and add 1 to it plus the sum
'''
x,y = map(int,input().split())
if x == 0 and y == 0:
    print("Not a moose")
elif x == y:
    print(f"Even {x+y}")
else:
    print(f"Odd {max(x,y)*2}")
