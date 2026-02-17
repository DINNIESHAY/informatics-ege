def f(n):
    s1 = f'{n:b}'
    if s1[-1] == '0':
        s2 = s1[:-1] + s1[0:2]
    else:
        return 0
    s3 = s2[::-1]
    return int(s3, 2)

for i in range(2, 1000):
    if f(i) == 119:
        print(i)