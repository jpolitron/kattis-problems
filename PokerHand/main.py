'''
Puesdo:
1. get the pair of inputs.
2. create a counter.
3. loop through and check the first letter of the string.
4. count those who are the same.
5. print out the  counter
'''
from collections import defaultdict
cards = [x[0] for x in input().split()]
counter = defaultdict(int)
for i in cards:
    counter[i] += 1
print(max(counter.values()))

#try to do something similar with a dictonary
