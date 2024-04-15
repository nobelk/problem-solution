def is_balanced(s: str) -> bool:
    stack = []

    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if not stack:
                return False
            top = stack.pop()
            if c == ')' and top != '(':
                return False
            if c == '}' and top != '{':
                return False
            if c == ']' and top != '[':
                return False
    # stack should be empty for balanced parenthesis
    return not stack
