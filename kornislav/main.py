'''
1. take in the 4 numbers
2. insert them into a set
3. calculate the max rectangle l * w
4. print the max

1 2 3 4 out 3
4 4 3 4 out 12
'''
def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    x = 0
    while swapped:
        swapped = False
        x += 1
        for i in range(len(nums) - x):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
max = 0
nums = list(map(int,input().split()))
bubble_sort(nums)
max = nums[0] * nums[2]
print(max)
