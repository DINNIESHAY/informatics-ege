def f(n):
    s = list(map(int, str(n)))
    s1 = 0
    for a in s:
        if a % 2 == 0:
            s1 += a
    d = str(n)
    s2 = sum(map(int, d[::2]))
    return abs(s1 - s2)

for i in range(1, 10000000):
    if f(i) == 28:
        print(i)
        break