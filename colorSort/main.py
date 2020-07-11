#givin array -> [{2},0,2|1,1,{0}]
# first step: divide the array in half and have a marker at each one
#-> [0,{0},2|1,{1},2]
# check the second numbers and if they are fine
#-> [0,0,{2}|{1},1,2]
#check which is bigger than switch
#-> [0,0,{1}|{2},1,2]
#after check if the first half is sorted if so leave it
#other wise > [0,0,1|{2},{1},2] final -> [0,0,1,1,2,2]
def color_sort(nums):
    def swap(i,j):
        nums[i],nums[j] = nums[j], nums[i]

    n = len(nums)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if nums[i-1] > nums[i]:
                swap(i-1,i)
                swapped = True

print(color_sort([2,0,2,1,1,0]))
print(color_sort([0,1,0,1,2,1]))
