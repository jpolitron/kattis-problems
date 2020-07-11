'''
Puesdo:
1. use the datime library and import date.
2. have a days list.
3. take in day and month.
4. then have the date in a the date library format.
5. look for the date in the days library by getting it from the .weekday bulit in function.
6. print it out
'''
from datetime import date

days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
]
day, month = map(int,input().split())
date = date(2009, month, day)
print(days[date.weekday()])
