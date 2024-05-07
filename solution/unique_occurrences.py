from collections import Counter

def uniqueOccurrences(arr):
    c = Counter(arr)
    o = []
    for k, v in c.items():
        o.append(v)
    sorted_o = sorted(o)
    for i in range(len(sorted_o) - 1):
        if sorted_o[i] == sorted_o[i + 1]:
            return False
    return True