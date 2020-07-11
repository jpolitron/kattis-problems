'''
Puesdo:
1. take in the # of cases
2. creat a for loop that takes in two strings
3. compare each letter if their the same add a . to the result
4. else if there different add a * to the result
5. print the result
'''
cases = int(input())
result = ""

for i in range(cases):
    first = str(input())
    second = str(input())
    print("\n")
    for index in range(len(first)):
        if first[index] == second[index]:
            result += '.'
        else:
            result += '*'
    print("\n")
    print(first, second, result, sep="\n")
    result = ""
