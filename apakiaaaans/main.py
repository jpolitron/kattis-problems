'''
Puesdo:
1. take in string
2. remove all the same repeats
3. print the final string
'''
last = ''
result = ''
for i in input().strip():
    if last != i:
        result += i
    last = i
print(result)
