'''
Puesdo:

'''
cases = int(input())
for i in range(cases):
    a,b,c = map(int,input().split())
    if a + b == c or b + a == c:
        print('Possible')
    elif a - b == c or b - a == c:
        print('Possible')
    elif a * b == c or b * a == c:
        print('Possible')
    elif a / b == c or b / a == c:
        print('Possible')
    else:
        print('Impossible')
