from typing import Dict

def is_valid_anagram(word1: str, word2: str) -> bool:
    tally: Dict[str, int] = {}
    word1_arr = list(word1.lower())
    for letter in word1_arr:
        if letter in tally:
            tally[letter] = tally[letter] + 1
        else:
            tally[letter] = 1

    word2_arr = list(word2.lower())
    for letter in word2_arr:
        if letter in tally:
            tally[letter] = tally[letter] - 1
        else:
            return False

    for key in tally.keys():
        if tally[key] != 0:
            return False
    return True
