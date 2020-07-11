'''
Puesdo:
1. take input as a string
2. create a counter for each kind of card (T,C,G) and score
3. add to specific counter whem looping
4. add to score using pow conter ** 2
5. check if there is three of a kind using min *7
6. print score

shorter version
1.take input.
2. use count function.
3. get min opf all 3
4. add score by coubter ** 2 for each card plus the min
'''
score = 0
s = str(input())
t = s.count('T')
c = s.count('C')
g = s.count('G')
x = min(t,c,g) * 7
score += (t**2 + c**2 + g**2 + x)
print(score)
