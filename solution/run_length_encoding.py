def get_run_length_encoding(string):
    if len(string) == 0:
        return ""
    elif len(string) == 1:
        return '1' + string
    prev = string[0]
    counter = 1
    result = []
    for index in range(1, len(string)):
        curr = string[index]
        if curr == prev:
            if counter < 9:
                counter += 1
            else:
                result.append(str(counter))
                result.append(prev)
                counter = 1
        else:
            result.append(str(counter))
            result.append(prev)
            counter = 1
        prev = curr

    result.append(str(counter))
    result.append(string[len(string) - 1])

    return "".join(result)
