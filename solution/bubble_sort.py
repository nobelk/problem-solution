def bubble_sort(array):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                is_swapped = True
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
    return array
