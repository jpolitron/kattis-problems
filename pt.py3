import sys

winner = 0;
winning_total = 0;
line_num = 0;

for line in sys.stdin:
	score = line.split();
    line_num = line_num + 1;
    current_total = int(score[0])+int(score[1])+int(score[2])+int(score[3]);
#int(score[3]);
    if current_total > winning_total:
       winning_total = current_total;
       winner = line_num;
print (winner, " ", winning_total);


