


def sort_cycle_shift(s, dp=None):
    n = len(s)
    p,c = [0]*n,[0]*n
    cnt = [0]*256
    for char in s:
        cnt[ord(char)] += 1
    for i in range(1,len(cnt)):
        cnt[i] += cnt[i-1]
    for i in range(n-1,-1,-1):
        j = ord(s[i])
        cnt[j] -= 1
        p[cnt[j]] = i
    classes = 1
    c[p[0]] = 0
    for i in range(1,n):
        if s[p[i]] != s[p[i-1]]:
            classes += 1
        c[p[i]] = classes - 1
    if dp is not None: dp.append(c)

    k = 0
    while (1 << k) < n:
        pn,cn = [0]*n,[0]*n
        for i in range(n):
            pn[i] = p[i] - (1 << k)
            if pn[i] < 0: pn[i] += n

        cnt = [0] * classes
        for i in range(n):
            cnt[c[pn[i]]] += 1
        for i in range(1,len(cnt)):
            cnt[i] += cnt[i-1]
        for i in pn[::-1]:
            j = c[i]
            cnt[j] -= 1
            p[cnt[j]] = i
        classes = 1
        cn[p[0]] = 0
        prev = (c[p[0]], c[(p[0] + (1 << k)) % n])
        for i in p[1:]:
            curr = (c[i], c[(i + (1 << k)) % n])
            if curr != prev:
                classes += 1
            cn[i] = classes - 1
            prev = curr
        if dp is not None: dp.append(cn)
        c = cn
        k += 1

    return p

def suffix_array(s, dp=None):
    p = sort_cycle_shift(s + "$", dp)
    return p[1:]

#nlogn, kasai's algorithm
def lcp_array(s, p=None):
    if p is None: p = suffix_array(s)
    n = len(s)
    rank = [0]*n
    for i in range(n):
        rank[p[i]] = i

    k = 0
    lcp = [0]*(n-1)
    for i in range(n):
        if rank[i] == n-1:
            k = 0
            continue
        j = p[rank[i] + 1]
        while i+k<n and j+k<n and s[i+k]==s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k: k -= 1
    return lcp


def sparse_table_min(arr):
    n = len(arr)
    st = [[0]*26 for _ in range(n)]
    for i in range(n):
        st[i][0] = arr[i]

    for j in range(1, 26):
        for i in range(n - (1 << j) + 1):
            st[i][j] = min(st[i][j-1], st[i + (1 << (j - 1))][j-1])
    return st


def longest_common_prefix_lcp_array(s):
    p = suffix_array(s)
    lcp = lcp_array(s, p)
    st = sparse_table_min(lcp)

    def RMQ(l,r):
        k = 0
        while (1<<(k+1)) <= r-l+1:
            k += 1
        return min(st[l][k], st[r - (1 << k) + 1][k])

    def lcp_query(i, j):
        l,r = p[i],p[j]
        if r < l: l,r = r,l
        return RMQ(l,r-1)

    print(lcp_query(0,3)) #ab
    print(lcp_query(1,2)) #b
    print(lcp_query(0,2)) # None

print(lcp_array("abbabd"))
longest_common_prefix_lcp_array("abbabd")
