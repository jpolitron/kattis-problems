def merge_sorted_arrays(nums1, nums2):
	nums1_index = 0
	nums2_index = 0

	while nums2_index < len(nums2):
		if nums2[nums2_index] <= nums1[nums1_index] or nums1[nums1_index] == 0:
			#nums1.insert(nums1_index, nums2[nums2_index])
			#nums1.pop()
			nums1.insert(nums1_index, nums2[nums2_index])
			nums1.pop()
			nums2_index += 1
		else:
		   nums1_index += 1


first_list = [1,2,3,0,0,0]

second_list = [2,5,6]

merge_sorted_arrays(first_list,second_list)

print(first_list)
print(second_list)
