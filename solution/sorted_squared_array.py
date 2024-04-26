def sortedSquaredArray(array):
    sorted_array = sorted(array, key=lambda x: abs(x))
    result = [x*x for x in sorted_array ]
    # Write your code here.
    return result
