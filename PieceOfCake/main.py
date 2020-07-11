'''
Puesdo:
1.take in n,h,v from user.
2. determine the biggest from h and n-h * max(v,n-v)*4
3. print result
'''
n, h, v = map(int, input().split())
result = max(h, n-h)*max(v, n-v)*4
print(result)
