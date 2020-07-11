'''
Puesdo:
in:
c-> #seed 1 square metre 2
l-> # of lawns           3
l lines -> w / l         2 3 = 6
                         4 5 = 20 } = 56 X 2 = 112
                         5 6 = 30
1. take in cost.
2. take in the number of lawns.
3. take in both length and width using a for loop and split.
4. multiply the length and width and add to result then times it by cost.
5. print result
'''
from decimal import Decimal
cost = float(input())
lawns = int(input())
result = 0
for i in range(lawns):
    l,w = map(float, input().split())
    result += Decimal(l*w)
result *= Decimal(cost)
print(round(result,8))
