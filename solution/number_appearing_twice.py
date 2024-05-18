

def single_number(nums):
    num = 0
    for n in nums:
        num ^= n
    return num