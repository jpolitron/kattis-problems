def pascalTriangle(numRows):
	triangle = [];
	for i in range(numRows):
		row = [];
		row.append(1);
		for j in range(i):
			left = row[i -1][j-1];
			right = row[i-1][j];
			row.append(left + right);
			row[len(row)-1] = 1;
			#adds the list to triangle
		triangle.append(row);
print(pascalTriangle(5))
print(pascalTriangle(3))
