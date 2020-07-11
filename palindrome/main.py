A = str(input())
result = 0
if len(A) > 0:
	i = 0
	while i < len(A):
		if (not A[i].isalnum()):
			A.strip(A[i])
		else:
			i+= 1
			for i in range(0,len(A)):
				j = len(A)-1-i
				if A[i].lower() != A[j].lower():
					result = 1
print(result)
