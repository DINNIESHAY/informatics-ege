from itertools import permutations
from itertools import product

words = []
for s1 in permutations('мари', 4):
    for s2 in product('ина', repeat = 4):
        s = ''.join(s1) + ''.join(s2)
        words.append(s)

words = sorted(words)
print(words.index('марианна') + 1)