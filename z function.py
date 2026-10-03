




def zfunction(arr):
    z = [0]*len(arr)
    l,r = 0,0
    for i in range(1, len(arr)):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        while i+z[i] < len(arr) and arr[z[i]] == arr[i+z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            l,r = i,i+z[i]-1
    return z

"""
print(zfunction("aaaaa"))
print(zfunction("aaabaab"))
print(zfunction("abacaba"))
"""



"""
Application
"""

def search_pattern(pattern, text):
    z = zfunction(pattern + "#" + text)
    m,n = len(pattern), len(text)
    start_pos = []
    for i in range(m+1, len(z)):
        if z[i] == m:
            start_pos.append(i-m-1)
    return start_pos

#print(search_pattern("aaa", "aaaaaabaababaaaa"))

def number_of_distinct_substring_o_n2(s):
    cnt = 1
    for i in range(1, len(s)):
        z = zfunction(s[:i+1][::-1])
        zmax = max(z)
        cnt += len(z) - zmax
    return cnt

"""
print(number_of_distinct_substring_o_n2("aaaaa")) #5
print(number_of_distinct_substring_o_n2("aabbabaa")) #27
print(number_of_distinct_substring_o_n2("aabccdzefbabaa")) #95
"""

def string_compression(s):
    z = zfunction(s)
    for i in range(1,1+len(s)):
        if len(s) % i == 0 and i+z[i] == len(s):
            return s[:i]
    return s

print(string_compression("aabaabaabaab"))
print(string_compression("aaaaa"))
print(string_compression("aabaab"))
