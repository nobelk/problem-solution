def find_pair(arr, targetSum):
    left, right = 0, len(arr)-1
    while (left < right):
        current_sum = arr[left]+arr[right]
        if current_sum == targetSum:
            return [left, right]

        if targetSum > current_sum:
            left += 1
        else:
            right -= 1
    return [-1, 1]