r = int(input())
triangle = []
if r == 0:
	print([])
elif r == 1:
	print([1])
else:
	for i in range(r):
		triangle.append([])
		triangle[i].append(1)
		triangle[0] = [1]
		for j in range(1,i):
			triangle[i].append(triangle[i-1][j-1]+triangle[i-1][j])
		if(r != 0):
			triangle[i].append(1)
	print(triangle)

