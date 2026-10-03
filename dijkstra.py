
        def dijkstra(start, adj):
            dist = [float("inf")]*n
            dist[start] = 0
            q = [(0,start)]
            while q:
                d,u = heappop(q)
                if d > dist[u]: continue
                for v,w in adj[u]:
                    if dist[v] > d+w:
                        dist[v] = d+w
                        heappush(q, (d+w, v))
            return dist