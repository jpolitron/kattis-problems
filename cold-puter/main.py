'''
Puesdo:
1. take in number of cases.
2. take in temps in one line.
4. create counter that counts tenps below 0
5. print out counter
'''
line = int(input().strip())
temps = str(input().strip()).split()
count = 0
for i in temps:
    if int(i) < 0:
        count += 1
    else:
        pass
print(count)
