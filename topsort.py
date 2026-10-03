

indeg = [0]*n
res = []

q = deque([i for i in range(n) if indeg[i] == 0])
while q:
    node = q.popleft()
    res.append(node)
    for neigh in adj[node]:
        indeg[neigh] -= 1
        if indeg[neigh] == 0:
            q.append(neigh)

if len(res) < n:
    return []
return res[::-1]
