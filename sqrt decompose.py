




#example use
        n = len(baskets)
        m = int(n**0.5)
        section = (n+m-1) // m

        blocks = [0]*section
        for i in range(n):
            blocks[i // m] = max(blocks[i // m], baskets[i])
        
        res = 0
        for f in fruits:
            remains = 1
            for b in range(section):
                if blocks[b] < f: continue
                k = 0
                blocks[b] = 0
                selected = False
                for j in range(m):
                    i = b * m + j
                    if i < n and baskets[i] >= f and not selected:
                        selected = True
                        baskets[i] = 0
                    if i < n:
                        blocks[b] = max(blocks[b], baskets[i])
                remains = 0
                break
            res += remains
        
        return res