def caesarCipherEncryptor(string, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for char in string:
        idx = alphabets.index(char)
        shifted_idx = (idx + key) % len(alphabets)
        result.append(alphabets[shifted_idx])
    return "".join(result)