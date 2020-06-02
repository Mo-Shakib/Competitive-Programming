x = int(input())
inn = out = 0
for positive in range(0, x):
    n = int(input())
    if 10 <= n <= 20:
        inn += 1
    else:
        out += 1
print(inn,'in')
print(out,'out')


