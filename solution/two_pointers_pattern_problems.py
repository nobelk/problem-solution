def find_pair_with_target_sum(arr: list[int], target_sum: int) -> list[int]:
    left_ptr = 0
    right_ptr = len(arr) - 1
    while left_ptr < right_ptr:
        if arr[left_ptr] + arr[right_ptr] == target_sum:
            return [left_ptr, right_ptr]
        elif arr[left_ptr] + arr[right_ptr] < target_sum:
            left_ptr += 1
        else:
            right_ptr -= 1
    return [-1, -1]