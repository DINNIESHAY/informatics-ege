from itertools import product

k = 0
words = [''.join(x) for x in product('1010S0111', repeat = 4)]
for word in words:
    if word.count('1') + word.count('S') == word.count('0') and '0S' not in word and 'S0' not in word:
        k += 1
print(k)
