def f(n):
   step1 = f'{n:b}'
   if n % 2 == 0:
       step2 = step1 + bin(sum(map(int, step1)))[2:]
   else:
       step2 = '1' + step1 + '00'
   return int(step2, 2)

for i in range(1, 1000):
    if f(i) > 215:
        print(i)
        break