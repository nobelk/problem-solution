def find_longest_chain(pairs: list[list[int]]):
    max_length = 0
    pairs.sort(key=lambda x: x[1])
    current_end = float('-inf')

    for pair in pairs:
        if pair[0] > current_end:
            max_length += 1
            current_end = pair[1]

    return max_length
