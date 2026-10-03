


#find all pattern s from string t
def rabin_karp(s, t):
    p = 31
    MOD = 1000000007

    ppow = [1]
    for i in range(max(len(s), len(t))):
        ppow.append((ppow[-1]*p) % MOD)

    h = [0]
    for i in range(len(t)):
        h.append((h[-1] + (ord(t[i]) - 97 + 1) * ppow[i]) % MOD)

    hs = 0
    for i in range(len(s)):
        hs = (hs + (ord(s[i]) - 97 + 1) * ppow[i]) % MOD

    res = []
    for i in range(len(t)-len(s)+1):
        if (hs * ppow[i]) % MOD == (MOD + h[i+len(s)] - h[i]) % MOD:
            res.append(i)
    return res



#find all pattern s from string t
def rabin_karp_enhanced(s, t):
    p = 31
    p2 = 29
    MOD = 1000000007

    ppow = [1]
    ppow2 = [1]
    for i in range(max(len(s), len(t))):
        ppow.append((ppow[-1]*p) % MOD)
        ppow2.append((ppow2[-1]*p2) % MOD)

    h = [0]
    h2 = [0]
    for i in range(len(t)):
        h.append((h[-1] + (ord(t[i]) - 97 + 1) * ppow[i]) % MOD)
        h2.append((h2[-1] + (ord(t[i]) - 97 + 1) * ppow2[i]) % MOD)

    hs = 0
    hs2 = 0
    for i in range(len(s)):
        hs = (hs + (ord(s[i]) - 97 + 1) * ppow[i]) % MOD
        hs2 = (hs2 + (ord(s[i]) - 97 + 1) * ppow2[i]) % MOD

    res = []
    for i in range(len(t)-len(s)+1):
        if (hs * ppow[i]) % MOD == (MOD + h[i+len(s)] - h[i]) % MOD and \
            (hs2 * ppow2[i]) % MOD == (MOD + h2[i+len(s)] - h2[i]) % MOD :
            res.append(i)
    return res



testcase = [
["aaabaaa","aa"],
["aaabaaa","aaa"],
]

for string,pattern in testcase:
    print(string,pattern,rabin_karp(pattern,string))
    print()



def minStartingIndex(self, s, pattern):
    """
    :type s: str
    :type pattern: str
    :rtype: int
    """
    def letter_diff(start_pos):
        cnt = 0
        for k in range(len(pattern)):
            if pattern[k] != s[start_pos+k]:
                cnt += 1
                if cnt >= 2: return False
        return True

    p = 31
    MOD = 1000000007

    pp = 1
    ppow = [1]
    hs = 0
    h = 0
    for i in range(len(pattern)):
        ppow.append((ppow[-1]*p) % MOD)
        hs = (hs*p + ord(pattern[i])) % MOD
        h = (h*p + ord(s[i])) % MOD
        if i: pp = (pp * 31) % MOD

    seen = set([hs])
    for i in range(len(pattern)):
        delta = 97 - ord(pattern[i])
        for diff in range(delta,delta+26):
            new_h = (MOD + hs + ppow[len(pattern)-1-i]*diff) % MOD
            seen.add(new_h)


    if h in seen and letter_diff(0):
        return 0

    i = 0
    while i + len(pattern) < len(s):
        h = ((h - ord(s[i])*pp)*p + ord(s[i+len(pattern)])) % MOD
        i += 1
        if h in seen and letter_diff(i):
            return i

    return -1
