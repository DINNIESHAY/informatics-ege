from itertools import product

k = 0
nums = set(''.join(x) for x in product('01234567', repeat = 5))
for num in nums:
    if num[0] == '7' and (num.count('65') == 1 or num.count('56')== 1) and not('65' in num and '56' in num) and int(num, 8) % 2 == 0:
        k += 1
print(k)
