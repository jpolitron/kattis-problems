'''
1. take in hands and trump.
2. take in # and suit while the user keeps inputing numbers.
3. check suit with trump.
4. if it checks out add it to sum using the suit function with the #.
5. else do the same but with the value function.
6. return the sum.
'''
hand, trump = input().split(" ")
limit = int(hand) * 4
sum = 0
def get_points(number, suit):
    scores = {"A": (11, 11),
              "K": (4, 4),
              "Q": (3, 3),
              "J": (20, 2),
              "T": (10, 10),
              "9": (14, 0),
              "8": (0, 0),
              "7": (0, 0)
              }
for i in range(limit):
    x = input()
    if x[1] == trump:
        sum += get_points(x[0],x[1])
    else:
        sum += get_points(x[0],x[1])
print(sum)
