def find_semordnilap(words):
    result = []
    dict = {}
    for word in words:
        if word[::-1] in dict:
            result.append([word[::-1], word])
        else:
            dict[word] = word

    # Write your code here.
    return result
