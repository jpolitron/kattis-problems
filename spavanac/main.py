'''
Pseudo:
1. take in hour and minutes
2. subtract 45 minutes
3. use the time library
'''
hour, min = map(int,input().split())

hour -= 1
min += 15

if hour < 0:
    hour += 24
if min >= 60:
    min -= 60
    hour += 1
print(str(hour) + " " + str(min))
