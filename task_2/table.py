print('x y z w | F')
print('-----------')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= y) and (y <= z) and (z <= w))
                print(f'{x} {y} {z} {w} | {int(f)}')