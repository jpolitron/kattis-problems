'''
1. take in 2 numbers num,denom
2. use an infinte loop to take in numbers
3. and check if they equal 0 0
4. else divide num by denom proper fraction
6. mod both numbers and thats the new num
6. print over denom
'''

while 1:
    num,denom = map(int,input().split())
    if num == 0 and denom == 0:
        break
    else:
        print(f"{int(num/denom)} {num%denom} / {denom}")
