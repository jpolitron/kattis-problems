'''
Puesdo:
1. take in the amount of gigs per month
2. take in the number of months
3. then have the total amount of gigs in those months
4. take in the amount used of each month
5. subtract the total
6. finallly return the total of gigs used
'''

x = int(input())
months = int(input())
total = x * (months + 1)

for i in range(1, months+1):
    mb = int(input())
    total -= mb
print(total)
