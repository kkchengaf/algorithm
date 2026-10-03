

m = 1001

def countsort(arr):
    res = [0] * len(arr)
    l,r = min(arr),max(arr)
    bucket = [0]*(r-l+1)
    for v in arr:
        bucket[v-l] += 1
    for i in range(1, r-l+1):
        bucket[i] += bucket[i-1]
    for i in range(len(arr)-1,-1,-1):
        bucket[arr[i]-l] -= 1
        res[bucket[arr[i]-l]] = arr[i]
    return res




print(countsort([999,56,78,0,333,45,23,333,4,55]))
print(countsort([999,56,-1000,50000,-67834,78,0,333,45,23,333,4,55]))
print(countsort([1,2,3,4,5,6]))
print(countsort([6,5,4,3,2,1]))
