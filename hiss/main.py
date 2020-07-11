'''
Puesdo:
1. take in the string from the user.
2. check if the last two elemtents of the string are ss
3. print hiss or no hiss depending on this condition.
'''
input = str(input())
flag = "hiss"

if len(input) > 1:
    if "ss" in input:
        print(flag)
    else:
        flag = "no hiss"
        print(flag)
