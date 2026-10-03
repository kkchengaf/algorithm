
        comb = [[0]*(n+1) for _ in range(n+1)]
        comb[0][0] = 1
        for i in range(1,n+1):
            for j in range(i+1):
                comb[i][j] = (comb[i-1][j-1] if j else 0) + comb[i-1][j]