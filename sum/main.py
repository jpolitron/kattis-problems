def sum_of_squares(k, b, n,i):
	sum1 = 0
	while n != 0:
		remainder = n % b
		n = int(n / b)
		sum1 += int(remainder**2)
	print((i + 1),sum1)

# read first line
number_of_lines = int(input())

# read all remaining lines
for i in range(number_of_lines):
 line = input()
 args = line.split();
 k = int(args[0]);
 b = int(args[1]);
 n = int(args[2]);

sum_of_squares(k, b, n, i)

