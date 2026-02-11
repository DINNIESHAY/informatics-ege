from itertools import permutations

k = 0
g = [''.join(x) for x in permutations('aaei', 2)]
c = [''.join(x) for x in permutations('kdmk', 2)]
words = set(''.join(x) for x in permutations('akademik'))
for word in words:
    if not(any(y in word for y in g)) and not(any(y in word for y in c)):
        k += 1
        print(word)
print(k)