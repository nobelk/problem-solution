WHITE, GREY, BLACK = 0, 1, 2


def cycleInGraph(edges):
    edge_color = [WHITE for _ in range(len(edges))]
    for node in range(len(edges)):
        if edge_color[node] != WHITE:
            continue
        contains_cycle = check_cycle(node, edges, edge_color)
        if contains_cycle:
            return True
    return False


def check_cycle(node, edges, edge_color):
    edge_color[node] = GREY
    neighbors = edges[node]

    for neighbor in neighbors:
        neighbor_color = edge_color[neighbor]
        if neighbor_color == GREY:
            return True
        if neighbor_color != WHITE:
            continue

        contains_cycle = check_cycle(neighbor, edges, edge_color)
        if contains_cycle:
            return True

    edge_color[node] = BLACK
    return False