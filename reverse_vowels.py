def reverse_vowels(sentence: str) -> str:
    if len(sentence) < 2:
        return sentence
    vowels = ['a', "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    s_array = list(sentence)
    left = 0
    right = len(sentence) - 1
    while left <= right:
        if s_array[left] in vowels and s_array[right] in vowels:
            temp = s_array[left]
            s_array[left] = s_array[right]
            s_array[right] = temp
            left = left + 1
            right = right - 1
        elif s_array[left] in vowels and s_array[right] not in vowels:
            right = right - 1
        elif s_array[right] in vowels and s_array[left] not in vowels:
            left = left + 1
        else:
            left = left + 1
            right = right - 1

    return "".join(s_array)
