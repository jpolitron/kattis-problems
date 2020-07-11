'''
Puesdo:
1. take in the number of cases
2. take in the numbers you will be taking in.
3. list of numbers
4. for loop through list and count the numbers
5. compare that count with 1
6. add that number to final themn clear list
7. print the odd man out and clear final

'''
cases = int(input())
final = 0 #keeps odd man
for i in range(cases):
    num = int(input()) #input the numbers taking in
    result = list(map(int,input().split())) #list of numbers taking in
    for j in result: #looping through list while counting the number
        if result.count(j) == 1: #check that it is only eqaul to 1
            final += j
    result.clear()
    print(f"Case #{i+1}: {final}")
    final = 0
