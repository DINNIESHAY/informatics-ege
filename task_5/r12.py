from itertools import permutations

def f(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    numbers = []
    for x1, x2 in list(permutations([d1, d2, d3], 2)):
        if 10 <= x1 * 10 + x2 <= 99:
            numbers.append(x1 * 10 + x2)
    return max(numbers) - min(numbers)

for i in range(100, 1000):
    if f(i) == 40:
        print(i)
        break