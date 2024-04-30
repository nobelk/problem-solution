def twoColorable(edges):
    colors = [None for _ in edges]
    colors[0] = True # start with the root
    stack = [0]

    while len(stack) > 0:
        node = stack.pop()
        for conn in edges[node]:
            if colors[conn] is None:
                colors[conn] = not colors[node]
                stack.append(conn)
            elif colors[conn] == colors[node]:
                return False
    return True