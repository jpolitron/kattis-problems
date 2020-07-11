'''
Psudeo:
1.take the string in.
2.loop through the string and have a counter for each category.
3. add the counters into a total
4. print out the category divided by the total
'''
spam = str(input())
white = 0
lower = 0
upper = 0
symbol = 0
for i in range(len(spam)):
    if spam[i] == '_':
        white += 1
    elif spam[i].islower() and spam[i].isalpha():
        lower += 1
    elif spam[i].isupper() and spam[i].isalpha():
        upper += 1
    else:
        symbol += 1
total = white + lower + upper + symbol
print(white/total,lower/total,upper/total, symbol/total, sep='\n')
