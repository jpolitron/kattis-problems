'''
Pseudo:
dividng tootal # bases hits by total # official bats
01234
1. take in bases
2. take in the hits length of bases
3. add those that are not negatives to score
4. while keeping track of numbers that were added to teh score
5. divide score by bases
'''
bases = int(input())
hits = list(map(int,input().split()))
score = 0
for i in range(len(hits)):
    if hits[i] < 0:
        bases -= 1
    else:
        score += hits[i]
print(score/bases)
