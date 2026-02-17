def f(n):
    d = list(map(int, str(n)))
    sums = sorted([d[0] + d[1], d[1] + d[2], d[2] + d[3]])
    return str(sums[1]) + str(sums[2])

for i in range(1000, 10000):
    if f(i) == '511':
        print(i)



