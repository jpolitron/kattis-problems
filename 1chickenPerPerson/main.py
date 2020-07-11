'''
Psuedo:
1. take in number of people and chicken.
2. create a count variable that keeps count of chicken pieces
3. then check that the amount of people is not the same as the chicken
4. if the amount of people is less than chicken subract it and get the absolute
5. print out Dr. Chaz will have 𝑃 piece[s] of chicken left over
6. else print the he needs more peices
'''
people, chicken = map(int,input().split())
count = abs(people - chicken)
if count >= 0:
    if people < chicken:
        print("Dr. Chaz will have %d %s of chicken left over!" % (count, piece))
    else:
        print("Dr. Chaz needs %d more %s of chicken!" % (count, piece))
