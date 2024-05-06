def findMaxAverage(nums, k):
    max_sum = 0
    for i in range(k):
        max_sum += nums[i]

    current_sum = max_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum / float(k)

