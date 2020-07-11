n = list(map(int,input().split()))
if len(n) == 1:
	n[len(n)-1] = n[len(n)-1]+1
	if n[len(n)-1] >= 10:
		x = []
		x.append(str(n[0]))
		x.append(str(n[1]))
		print(x)
	print(n)
else:
	n[len(n)-1] = n[len(n)-1]+1
	print(n)
