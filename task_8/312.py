from itertools import permutations

k = 0
c = 'МФБРХ'
words = set(''.join(x) for x in permutations('АМФИБРАХИЙ', 10))
for word in words:
    if word[1] in c and word[3] in c and word[5] in c and word[7] in c and word[9] in c:
        k += 1

print(k)