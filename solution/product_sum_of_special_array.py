# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

# Write a method that calculates the product sum of all elements within a special array
# Special array is an array that contains numbers or other arrays
def productSum(array):
    # Write your code here.
    return productSumHelper(array, 1)


def productSumHelper(array, depth):
    result = 0
    for num in array:
        if type(num) is list:
            result += productSumHelper(num, depth+1)
        else:
            result += num
    return depth*result