
x = 0
y = 0
z = 0

cases = int(input())

while cases != 0:
    x,y = map(int,input().split())
    print(str(x) + " ")
    v = vector()
    for i in range(y):
        temp = int(input())
        v.add(temp)

    s = vector(v)
    sort(s)
    index = 0
    for i in range(y):
        if v[i] == s[index]:
            index += 1
    cases -= 1
    print(y - index)
