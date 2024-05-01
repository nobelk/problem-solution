def moveElementToEnd(array, toMove):
    left_ptr = 0
    right_ptr = len(array) - 1
    while left_ptr < right_ptr:
        while left_ptr < right_ptr and array[right_ptr] == toMove:
            right_ptr -= 1
        if array[left_ptr] == toMove:
            array[left_ptr], array[right_ptr] =  array[right_ptr], array[left_ptr]
        left_ptr += 1
    return array
