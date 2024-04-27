def isMonotonic(array):
    if not array or len(array) <= 2:
        return True

    start_idx = 1
    if array[0] == array[1] and len(array) > 2:
        result = is_increasing(array[1], array[2])
        start_idx += 1
    else:
        result = is_increasing(array[0], array[1])

    for idx in range(start_idx, len(array) - 1):
        if array[idx] == array[idx + 1]:
            result == is_increasing(array[idx], array[idx + 1])
        elif result != is_increasing(array[idx], array[idx + 1]):
            return False
        else:
            result = is_increasing(array[idx], array[idx + 1])
    return True


def is_increasing(num1, num2):
    return num2 >= num1