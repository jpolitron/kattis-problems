def merge_sort(nums):
  result = []
  if len(nums) > 1:
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    i = 0
    j = 0
    k = 0
  
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        nums[k] = left[i]
        i = i + 1
      else:
        nums[k] = right[j]
        j = j + 1
      k = k + 1
    while i < len(left):
      nums[k] = left[i]
      i = i + 1
      k = k + 1
    while j < len(right):
      nums[k] = right[j]
      j = j + 1
      k = k + 1
      
    
  
  return nums
    
print(merge_sort([23,178,90,3,12,34]))
print(merge_sort([34,564,34,42536,8656,33,2,1]))
print(merge_sort([121,2,343,45353,12,1,0,55,54]))
