'''
Puesdo:
1. take in number of cases.
2. take miles and time
3. multiply speed and the result of current - previous and add to miles
4. have previous equal to current
5. and continue till the cases is done and take the next case and so forth.
6. print the miles
7. stop the program when the user enters -1
'''
import sys
cases = 0
while True:
    cases = int(input())
    if cases == -1:
        sys.exit()
    previous = 0
    miles = 0
    for i in range(cases):
        speed, current = map(int,input().split())
        miles += speed * (current - previous)
        previous = current
    print(f"{miles} miles")
