def f(x):
    step1 = str(x % 2)
    step2 = str(x % 3)
    step3 = str(x % 5)
    number = step1 + step2 + step3
    return int(number)

search = 10
while f(search) != 104:
    search +=1
print(search)



