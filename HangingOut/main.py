'''
Puesdo:
saftey limt, # events
# of people who leave will never exceed # people curently on terrance
1. take in limit and events/cases.
2. do a for loop to enter 2 and leave 1 the length of events.
3. have a counter that keeps track of groups that made it in

enter:  0 1
leave: 2
enter: 3 4

4 5
enter 3
enter 2
leave 1
enter 1
enter 2
'''
limit, events = map(int,input().split())
num = 0
counter = 0

for i in range(events):
    option, x = input().split()
    x = int(x)
    if option[0] == 'e':
        if num + x > limit:
            counter += 1
        else:
            num += x
    else:
        num -= x
print(counter)
