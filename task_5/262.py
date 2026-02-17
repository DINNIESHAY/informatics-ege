def f(n):
    if n % 2 == 0:
        step1 = n / 2
    else:
        step1 = n - 1
    if step1 % 3 == 0:
        step2 = step1 / 3
    else:
        step2 = step1 - 1
    if step2 % 5 == 0:
        step3 = step2 / 5
    else:
        step3 = step2 - 1
    return step3

count = 0
for i in range(2, 1000):
    if f(i) == 3:
        count +=1
print(count)