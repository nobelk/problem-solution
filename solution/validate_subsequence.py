def isValidSubsequence(array, sequence):
    index = 0
    for item in sequence:
        while index < len(array):
            if item == array[index]:
                break
            index += 1
        if index == len(array):
            return False
    return True
