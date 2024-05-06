

def highest_point(gains):
    current_alt = 0
    highest_point = current_alt
    for alt_gain in gains:
        current_alt += alt_gain
        highest_point = max(current_alt, highest_point)
    return highest_point