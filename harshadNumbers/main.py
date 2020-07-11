'''
1. create a function that will take in # and have a var x that will
add the single #'s using a for loop the goes through the list and
return whether it is true or false by num % x == 0.
2. take in the # from user.
3. create a list called result that holds the string version of num.
4. using a while loop determine if the statement is false by ! it
if the statment turns to false execute program and print the final num.
5. else add one to the number and update list with the num value and run
through the process again until the flag is false
'''
def is_harshad(num):
    x = 0
    for i in range(len(result)):
        x+= result[i]
    return num % x == 0

num = int(input())
result = list(map(int,str(num)))
while not is_harshad(num):
    num+=1
    result = list(map(int,str(num)))

print(num)
