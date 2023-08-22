def check_pangram(input_line: str):
    found: set[str] = set()
    for found_char in input_line.lower():
        found.add(found_char)
    return len(found) == 26
