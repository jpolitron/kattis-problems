'''
Psudeo:
1. take in the number of cases
2. take in the order
3. then split it into a list
4. iterate through the list and check the first index for the the key word 'simon'
5. if it passes the case then check the next index if it says 'says'
6. if so then start printing out the words seprated by a space.
7. once the order
8. then continue until cases are done
'''
cases = int(input())
for i in range(cases):
    order = str(input())
    if order.startswith("Simon says"):
        print(order[11:]) #11 because simon says is 11 characters
    else:
        print(end='')#makes sure there is not an extra line
