def moveElementToEnd(nums, toMove):
    last_item_to_move_at = 0
    for i in range(len(nums)):
        if nums[i] != toMove:
            nums[last_item_to_move_at] = nums[i]
            last_item_to_move_at += 1

    for i in range(last_item_to_move_at, len(nums)):
        nums[i] = toMove
    return nums
