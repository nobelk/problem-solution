def sqrt(x):
    if x == 0:
        return 0
    elif x < 2:
        return 1

    left, right = 0, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def sqrt1(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1

    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + float(x) / x0) / 2
    return int(x1)