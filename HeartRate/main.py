'''
Puesdo:
1. take in the number of cases.
2. take in beats and seconds using input().split().
3. have min apbm calculated by doing (b-1)* 60/ p.
4. have bpm calculated by doing b * 60/p.
5. finally calculate max abpm by doing (b+1)* 60/p.
6. print out results
'''
from decimal import Decimal
n = int(input())

for i in range(n):
    b,p = input().split()
    b = int(b)
    p = float(p)
    print(round((b-1)*60/p,4) , round(b*60/p,4) , round((b+1)*60/p,4))
