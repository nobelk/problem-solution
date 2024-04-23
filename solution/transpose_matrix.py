def transposeMatrix(matrix):
    result = []
    for column in range(len(matrix[0])):
        r = []
        for row in range(len(matrix)):
            r.append(matrix[row][column])
        result.append(r)
    # Write your code here.
    return result
