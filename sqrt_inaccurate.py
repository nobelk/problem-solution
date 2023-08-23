def get_inaccurate_sqrt_value(num: int):
    if num < 2:
        return num
    pivot = 0
    left_index, right_index = 2, num // 2
    while left_index <= right_index:
        pivot = left_index + (right_index - left_index) // 2
        cand = pivot * pivot
        if pivot * pivot > num:
            right_index = pivot - 1
        elif pivot * pivot < num:
            left_index = pivot + 1
        else:  # equal value
            return pivot
    return pivot
