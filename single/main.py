nums = list(map(int,input().split()))
nums.sort()
counter = 1
for i in range(1,len(nums)+1):
    if i != len(nums) and nums[i-1] == nums[i]:
        counter += 1
    elif counter == 2:
        counter = 1
    elif counter == 1:
        print(nums[i-1])
    else:
    	print(0)
