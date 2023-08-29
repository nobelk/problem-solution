def contains_duplicates(nums) -> bool:
    if len(nums) == 0:
        return False
    nums.sort()
    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            return True
    return False
