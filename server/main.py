n = int(input())
t = int(input())
sum = 0
for j in range(0,n):
	i = int(input())
	sum += i
	if sum > t:
		print(j)
		break
