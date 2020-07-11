'''
Psudeo:
1. take in l and h.
2. check if it meets the cuntraints 123456 <= L < H <= 987654.
3. have a counter for the number of possibilites
4. once that pass this test case we will check if it can be divisable by the #'s
'''
L,H = int(input().split())
if 123456 <= L and L < H and H <= 987654:
    for i in range(L):
        
