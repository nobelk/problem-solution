
def twoNumberSum(arr: list[int], targetSum: int):
    y_values_dict = {}
    result = []
    for num in arr:
        if y_values_dict.get(num):
            result = [num, y_values_dict.get(num)]
            break
        else:
            y_values_dict[targetSum - num] = num
    return result
