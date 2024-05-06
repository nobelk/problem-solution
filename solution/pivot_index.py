def find_pivot_index(nums):
    if len(nums) <= 1:
        return -1
    s = sum(nums)
    left_sum = 0
    for i, x in enumerate(nums):
        if left_sum == (s - left_sum - x):
            return i
        else:
            left_sum += x
    return -1
