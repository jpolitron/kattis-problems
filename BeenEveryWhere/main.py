'''
t = cases
n = # work trips
Puesdo:
1. take in cases.
2. take the # of work trips.
3. take in city names.
4. count the cities that show up atleast once
5. print result.
'''
cases = int(input())
result = set()
while cases != 0:
    n = int(input())
    for i in range(n):
        city = str(input())
        result.add(city)
    print(len(result))
    cases -= 1
    result.clear()
