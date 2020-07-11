'''
Puesdo:
1. Take in the string from user.
2. get the first letter of each string after -
3. store it in a string variable.
4. print result
'''
input = str(input())
result = ''
result += input[0]
for i in range(len(input)):
    if input[i] == '-':
        result += input[i+1]
    else:
        continue
print(result)
