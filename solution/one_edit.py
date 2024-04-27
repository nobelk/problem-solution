def oneEdit(stringOne, stringTwo):
    len1, len2 = len(stringOne), len(stringTwo)
    if abs(len1 - len2) > 1:
        return False

    idx1 = idx2 = 0

    skipped = False
    while idx1 < len1 and idx2 < len2:
        if stringOne[idx1] != stringTwo[idx2]:
            if skipped:
                return False
            else:
                skipped = True
            if len1 < len2:
                idx1 -= 1
            elif len2 < len1:
                idx2 -= 1
        idx1 += 1
        idx2 += 1

    return True