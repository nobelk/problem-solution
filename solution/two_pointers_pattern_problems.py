def find_pair_with_target_sum1(arr: list[int], target_sum: int) -> list[int]:
    left_ptr = 0
    right_ptr = len(arr) - 1
    while left_ptr < right_ptr:
        if arr[left_ptr] + arr[right_ptr] == target_sum:
            return [left_ptr, right_ptr]
        if arr[left_ptr] + arr[right_ptr] < target_sum:
            left_ptr += 1
        else:
            right_ptr -= 1
    return [-1, -1]


def remove_duplicates(arr: list[int]) -> int:
    next_non_duplicate = 1
    index = 0
    while index < len(arr):
        if arr[next_non_duplicate - 1] != arr[index]:
            arr[next_non_duplicate] = arr[index]
            next_non_duplicate += 1
        index += 1
    return next_non_duplicate


def make_squares(arr: list[int]) -> list[int]:
    r_list = [0 for x in range(len(arr))]
    left, right = 0, len(arr) - 1
    highest_square_index = len(arr) - 1
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            r_list[highest_square_index] = left_square
            left += 1
        else:
            r_list[highest_square_index] = right_square
            right -= 1
        highest_square_index -= 1
    return r_list


def search_triplets(arr: list[int]) -> list[list[int]]:
    arr.sort()
    triplets = []

    for index in range(len(arr)):
        if index > 0 and arr[index] == arr[index - 1]:
            continue
        find_pair_with_target_sum(arr, -arr[index], index + 1, triplets)
    return triplets


def find_pair_with_target_sum(arr: list[int], target_sum: int, left: int,
                              triplets: list[list[int]]):
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target_sum:
            triplets.append([arr[left], arr[right], -target_sum])
            left += 1
            right -= 1
        elif sum < target_sum:
            left += 1
        else:
            right -= 1


def dutch_flag_sort(arr: list[int]) -> list[int]:
    low = 0
    high = len(arr) - 1
    index = 0

    while index <= high:
        if arr[index] == 0:
            arr[index], arr[low] = arr[low], arr[index]
            low += 1
            index += 1
        elif arr[index] == 1:
            index += 1
        else:
            arr[index], arr[high] = arr[high], arr[index]
            high -= 1
    return arr
