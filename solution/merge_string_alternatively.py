def mergeAlternately(word1, word2):
    i, j = 0, 0
    word1_length = len(word1)
    word2_length = len(word2)
    result = []
    while i < word1_length or j < word2_length:
        if i < word1_length:
            result.append(word1[i])
            i += 1
        if j < word2_length:
            result.append(word2[j])
            j += 1
    return "".join(result)