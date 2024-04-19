def calculate_distance(words: list[str], word1: str, word2: str) -> int:
    minDistance = len(words)
    position1, position2 = -1, -1
    for i, word in enumerate(words):
        if word == word1:
            position1 = i
        elif word == word2:
            position2 = i
        if position1 != -1 and position2 != -1:
            minDistance = min(minDistance, abs(position1 - position2))
    return minDistance
