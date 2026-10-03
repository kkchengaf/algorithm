

adj = defaultdict(set)


def euler_path(adj, start):
    seq = []
    stack = [start]

    while stack:
        node = stack[-1]
        if len(adj[node]) == 0:
            seq.append(node)
            stack.pop()
        else:
            neigh = adj[node].pop()
            stack.append(neigh)
    return seq
