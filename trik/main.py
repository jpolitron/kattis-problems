'''
Puesdo:
1. create a string ABBA a is the ball
2. shift depening on the letters
3. output the location
'''
cups = ['D','O','O']
s = str(input())

for i in range(len(s)):
    if s[i] == 'A':
        temp = cups[0]
        cups[0] = cups[1]
        cups[1] = temp
    elif s[i] == 'B':
        temp = cups[1]
        cups[1] = cups[2]
        cups[2] = temp
    else:
        temp = cups[0]
        cups[0] = cups[2]
        cups[2] = temp
print(cups.index('D')+1)
