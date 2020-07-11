'''
Puesdo:
1. take in the string.
2. create a total of how long it will take to put his name.
3. loop through the string and check if a certain number doesnt contain a letter
4. count total
5. print total
'''
s = str(input())
total = 0

for i in range(len(s)):
    if i% 3 == 0 and s[i] != 'P':
        total += 1
    if i% 3 == 1 and s[i] != 'E':
        total += 1
    if i% 3 == 2 and s[i] != 'R':
        total += 1
print(total)
