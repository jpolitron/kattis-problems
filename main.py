rows = 5;

triangle = [];

for i in range(rows):
    row = [];
    row.append(1);
    for j in range(i):
        row.append(2+j);
    triangle.append(row);
    
print(triangle)
