def array_sign(nums: list[int]) -> int:
    count = 0
    for num in nums:
        if num == 0:
            return 0
        if num < 0:
            count += 1
    if count % 2 == 0:
        return 1
    else:
        return -1
