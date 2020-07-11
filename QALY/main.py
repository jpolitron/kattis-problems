'''
Puesdo:
1. take in the number of cases with a for loop
2. take both numbers wit split
3. multiply the two numbers and add them to the total
'''
#decimal library
from decimal import Decimal
#num fo cases
num = int(input())
total = 0
for i in range(0,num):
    #takes in both numbers and puts them in a list
    input = input().split()
    #puts float in decimal form and *'s the first and second number and adding it to total
    total += Decimal(float(input[0]) * float(input[1]))
    #deletes list inorder to get the new pair of numbers
    del input
    #sets precision to 3 decimal places
print(round(total,3))
