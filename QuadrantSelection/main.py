'''
Puesdo:
1. get the x and y from user.
2. check if the x and y are either 2:(-,+), 3:(-,-), 1:(+,+), 4:(+,-)
3. then return quadrant number.
'''
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)
