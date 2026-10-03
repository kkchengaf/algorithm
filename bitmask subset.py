

p = 10

res = []
for mask in range(1, 1<<p):
    # preprocess
    mul = 0

    for i in range(p):
        if (mask) & (1 << i):
            # do sth using arr[i]
            mul |= 1<<i

    #postprocess
    res.append(mul)

#print(res)


arr = [2,3,5,7,11,13,17,19]
res = []
for mask in range(1, 1<<len(arr)):
    # preprocess
    mul = 1

    for i in range(len(arr)):
        if (mask) & (1 << i):
            # do sth using arr[i]
            mul *= arr[i]

    #postprocess
    res.append(mul)

print(res)
