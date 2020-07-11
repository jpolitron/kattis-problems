'''
Puesdo:
1. take in user input
2. check if the month is either oct 31 or dec 25
'''
input = input().split()

if(len(input[0]) == 3):
    if ((input[0] == 'OCT' and input[1] == '31') or (input[0] == 'DEC' and input[1] == '25')):
        print('yup')
    else:
        print('nope')
