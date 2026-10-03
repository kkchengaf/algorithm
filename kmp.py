

# pmt[i] = k, s[:k] == s[i+1-k:i+1]
# when pmt[i] = k, this suffix ending at index i has the longest prefix of length k of this string
def kmp(ss):
    n = len(ss)
    pmt = [0]*n
    j = 0
    for i in range(1, n):
        while j and ss[i]!=ss[j]: j = pmt[j-1]
        if ss[i]==ss[j]: j += 1
        pmt[i] = j
    return pmt



"""

    Application

"""

def search_pattern(pattern, text):
    m,n = len(pattern),len(text)
    pmt = kmp(pattern + "#" + text)
    res = []
    for i in range(m+1, len(pmt)):
        if pmt[i] == m:
            res.append(i - 2*m)
    return res
"""
print(search_pattern("aaa", "aaaaa"))
print(search_pattern("aaabb", "aaabbaaabbaaabb"))
"""


def number_of_occurrence_of_prefix(s):
    pmt = kmp(s)
    cnt = [0] * (len(s)+1)
    for i in range(len(pmt)):
        cnt[pmt[i]] += 1
    for i in range(len(cnt)-1,0,-1):
        cnt[pmt[i-1]] += cnt[i]
    for i in range(1, len(cnt)):
        cnt[i] += 1
    return cnt

"""
print(number_of_occurrence_of_prefix("aaaaa"))
print(number_of_occurrence_of_prefix("aabaabaab"))
"""


def number_of_occurrence_of_prefix_of_pattern(pattern, text):
    pmt = kmp(pattern + "#" + text)
    cnt = [0] * (len(pattern)+1)
    m = len(pattern)
    for i in range(len(text)):
        cnt[pmt[m+1+i]] += 1
    for i in range(len(cnt)-1,0,-1):
        cnt[pmt[i-1]] += cnt[i]
    return cnt

"""
print(number_of_occurrence_of_prefix_of_pattern("aaaaa", "aaaaab"))
print(number_of_occurrence_of_prefix_of_pattern("aabaabaab","aabaabaab"))
"""

def string_compression(s):
    pmt = kmp(s)
    n = len(s)
    if n % (n - pmt[-1]) == 0: return s[:n - pmt[-1]]
    return s[:n]

"""
print(string_compression("aabaabaab"))
print(string_compression("aaaaa"))
print(string_compression("abcdef"))
"""


def number_of_distinct_substring_o_n2(s):
    res = 1
    for i in range(1,len(s)):
        pmt = kmp(s[:i+1][::-1])
        res += len(pmt)-max(pmt)
    return res

print(number_of_distinct_substring_o_n2("aaaaa")) #5
print(number_of_distinct_substring_o_n2("aabbabaa")) #27
print(number_of_distinct_substring_o_n2("aabccdzefbabaa")) #95


"""
["a","aba","ababa","aa"]
["pa","papa","ma","mama"]
["abab","ab"]
["b","b","bb"]
["bb","bb"]
["ccb","aa","bab","ccb"]
["a","c","cacaa","ccccc"]


#return starting index of all occurence of pattern in ss
def kmp(ss, pattern):
    res = []
    pmt = kmp(pattern)
    j = 0
    for i in range(len(ss)):
        while j and ss[i]!=pattern[j]: j = pmt[j-1]
        if ss[i]==pattern[j]: j += 1
        if j == len(pattern):
            start = i-j+1
            res.append(start)
            j = pmt[j-1]
    return res

pattern1 = "aaa"
words = "aaaaaaaaaaaa"

print(kmp(pattern1 + "#" + words)[len(pattern1)+1:])

def split_by_all_match(ss, pat):
    index = kmp(ss, pat)
    n = len(pat)
    for i in index:
        print(ss[:i], ss[i:i+n], ss[i+n:])
testcase = [
["aaabaaa","aa"],
["aaabaaa","aaa"],
]


for string,pattern in testcase:
    print(string,pattern,kmp(string,pattern))
    split_by_all_match(string,pattern)
    print()
"""
