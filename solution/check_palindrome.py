import string


def is_valid_palindrome(sentence: str) -> bool:
    if len(sentence) < 2:
        return True
    left = 0
    right = len(sentence) - 1
    while left <= right:
        if sentence[left] in string.punctuation \
                or sentence[left] in string.whitespace:
            left = left + 1
        elif sentence[right] in string.punctuation \
                or sentence[right] in string.whitespace:
            right = right - 1
        elif sentence[left].lower() == sentence[right].lower():
            left = left + 1
            right = right - 1
        else:
            return False
    return True
