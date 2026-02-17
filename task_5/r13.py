def f(n):
    step1 = f'{n:b}'
    step2a = step1 + str(sum(map(int, step1)) % 2)
    # map(int, step1) - превращает строку в последовательность чисел (например, "1010" в [1, 0, 1, 0])
    # sum(...) - складывает эти числа
    # str(sum(...) % 2) - получаем остаток от деления на 2 и превращаем в строку
    step2b = step2a + str(sum(map(int, step2a)) % 2)
    return int(step2b, 2)

search = 1
while f(search) <= 77:
    search += 1
print(search)