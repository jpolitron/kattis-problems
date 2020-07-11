def server_time_check(task_config, task_times):
  return 0
  

## Please do not change the code below this line
## These lines are how the tests interact with the code

task_config = input()
task_times = input()
list1 = list(map(int,task_config.split()))
list2 = list(map(int,task_times.split()))
sum = 0
for j in range(0,list1[0]):
  sum += list2[j]
  if sum > list1[1]:
    print(j)
    break
  

server_time_check(task_config, task_times)
