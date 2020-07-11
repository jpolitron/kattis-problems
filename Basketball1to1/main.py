'''
Psudeo:
1. take in the string.
2. whatever has A is going to go into A's points.
3. if its not A then its B's point.
4. if its a tie then if has to be win by 2 points
'''
score = str(input())
Alice = 0
Barbara = 0

for i in range(len(score)):
    if score[i] == 'A':
        Alice += int(score[i+1])
    elif score[i] == 'B':
        Barbara += int(score[i+1])

if Alice < Barbara:
    print('B')
elif Alice > Barbara:
    print('A')
