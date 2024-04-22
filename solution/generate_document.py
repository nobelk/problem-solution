def can_generate_document(characters, document):
    if len(document) == 0:
        return True
    dict = {}
    for ch in characters:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1

    for ch in document:
        if ch in dict:
            if dict[ch] <= 0:
                return False
            else:
                dict[ch] -= 1
        else:
            return False
    # Write your code here.
    return True
