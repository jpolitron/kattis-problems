'''
Psudeo:
1. take in cases.
2. create an empty list.
3. loop over and take in x and y then check if x is a digit.
4. then append x and y into the list else append them both.
5. sort list.
6. then loop through starting from the amount of cases all the way to the length.
'''
cases = int(input())
final = list()
for i in range(cases):
    x,y = map(str,input().split())
    if str.isdigit(x):
        x = int(x)/2
        final.append(str(x))
        final.append(str(y))
    else:
        final.append(str(x))
        final.append(str(y))
final.sort()
for j in range(cases,len(final)):
    print(final[j])
