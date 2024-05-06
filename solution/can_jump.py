


def can_jump(nums):
    GOOD, UNKNOWN = 0, -1
    memo = [UNKNOWN]*len(nums)
    memo[-1] = GOOD
    for i in range(len(nums)-2, -1, -1):
        farthest_jump = min(i+nums[i], len(nums))
        for j in range(i, farthest_jump+1):
            if memo[j] == GOOD:
                memo[i] = GOOD
                break
    return memo[0] == GOOD