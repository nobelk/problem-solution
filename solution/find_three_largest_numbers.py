def findThreeLargestNumbers(array):
    result = [float('-inf'), float('-inf'), float('-inf')]
    for item in array:
        insert_into_arr(result, item)
    return result


def insert_into_arr(arr, val):
    if val > arr[2]:
        arr[0] = arr[1]
        arr[1] = arr[2]
        arr[2] = val
    elif val > arr[1]:
        arr[0] = arr[1]
        arr[1] = val
    elif val > arr[0]:
        arr[0] = val
    return arr
