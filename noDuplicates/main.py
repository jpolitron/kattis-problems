'''
Puesdo:
1. take in original.
2. convert that in a new varaible changed and insert into a set.
3. check the lengths if there the same then print yes
4. else print no
'''

original = input().split()
changed = set(original)
if len(original) == len(changed):
    print("yes")
else:
    print("no")
