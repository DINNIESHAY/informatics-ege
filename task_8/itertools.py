from itertools import product, permutations, combinations, combinations_with_replacement

# product - размещения с повторениями
words = product('AB', repeat=3)
for w in words:
    print(''.join(w))

# permutations - перестановки
perms = permutations('КОТ')
for p in perms:
   print(''.join(p))

# combinations - сочетания без повторений
coms = combinations('ABC', 2)
for c in coms:
   print(''.join(c))

# combinations_with_replacement - сочетания с повторениями
coms = combinations_with_replacement('ABC', 2)
for c in coms:
    print(''.join(c))