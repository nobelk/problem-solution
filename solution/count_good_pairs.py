def count_good_pairs(nums: list[int]) -> int:
    pairCount = 0
    pairs = {}
    for num in nums:
        pairs[num] = pairs.get(num, 0) + 1
        pairCount += pairs[num] - 1
    return pairCount