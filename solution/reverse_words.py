

def reverse_words(s):
    s.strip()
    l = s.split() # cannot use s.split(' ')
    for i in range(len(l)):
        l[i] = l[i].strip()
    l = reversed(l)
    return " ".join(l).strip()