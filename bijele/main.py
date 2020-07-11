'''
1. have a list of original pieces
2. take in the pieces
3. loop through the original and subtract the n
'''
og = [1,1,2,2,2,8]
n = list(map(int, input().split()))

for i in range(len(og)):
    og[i] -= n[i]
    print(og[i], end=" ")
