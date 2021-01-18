def selection_sort(nums):
    n = len(nums)

    for bottom in range(n-1):
        smallest_index = bottom
        for i in range(bottom + 1, n):
            if nums[i]< nums[smallest_index]:
                smallest_index = i
        nums[bottom], nums[smallest_index] = nums[smallest_index], nums[bottom]

    return nums

print(selection_sort([4,3,7,1,2,3,-4,4,5]))