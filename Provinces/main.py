'''
psudeo:
1. get amount of gold, sliver, and copper.
2. depending on those how much buying powder you have also known as total.
3. check the victory firsdt then check the treasure using if statements wit total.
'''
gold, silver, copper = map(int,input().split())
total = gold * 3 + silver *2 + copper

#checking victory cards with total
def victory(total):
    if total > 1:
        if total > 7:
            return 'Province'
        elif total > 4:
            return 'Duchy'
        elif total > 1:
            return 'Estate'

#checking the treasure cards with total
def treasure(total):
    if total > 5:
        return 'Gold'
    elif total > 2:
        return 'Silver'
    else:
        return 'Copper'
#if total is 2 or greater this means you can have either card else only from treasure
if total >= 2:
    print("{} or {}".format(victory(total),treasure(total)))
else:
    print(treasure(total))
