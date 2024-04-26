def selectionSort(array):
    for index in range(len(array)):
        smallest_index, _ = min(enumerate(array[index:]), key=lambda x: x[1])
        array[index], array[smallest_index + index] = array[smallest_index + index], array[index]
    return array
