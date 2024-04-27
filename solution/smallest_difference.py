def smallestDifference(arrayOne, arrayTwo):
    minDiff = float('inf')
    minPair = []
    # Write your code here.
    for num1 in arrayOne:
        for num2 in arrayTwo:
            if diff(num1, num2) < minDiff:
                minDiff = diff(num1, num2)
                minPair = [num1, num2]

    return minPair


def diff(num1, num2):
    if num1 * num2 > 0:
        return abs(num1 - num2)
    elif num1 > num2:
        return abs(num1 - num2)
    else:
        return abs(num2 - num1)
