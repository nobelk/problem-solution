from collections import Counter

def closeStrings(word1, word2):
    wc1 = Counter(word1)
    wc2 = Counter(word2)

    wc1_key_list = [key for key in wc1.keys()]
    wc1_keys = sorted(wc1_key_list)
    wc2_key_list = [key for key in wc2.keys()]
    wc2_keys = sorted(wc2_key_list)

    wc1_value_list = [value for value in wc1.values()]
    wc1_values = sorted(wc1_value_list)
    wc2_value_list = [value for value in wc2.values()]
    wc2_values = sorted(wc2_value_list)

    return wc1_keys == wc2_keys and wc1_values == wc2_values