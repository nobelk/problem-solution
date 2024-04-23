

def commonCharacters(string):
    counter_map = {}
    for s in string:
        unique_chars = {}
        for index in range(len(s)):
            ch = s[index]
            if ch not in unique_chars:
                unique_chars[ch] = 1
        for ch in unique_chars:
            if ch in counter_map:
                counter_map[ch] += 1
            else:
                counter_map[ch] = 1
    result = []
    count = len(string)
    for ch in counter_map:
        if counter_map[ch] == count:
            result.append(ch)
    return result