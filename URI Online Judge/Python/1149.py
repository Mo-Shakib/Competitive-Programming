lista = list(map(int, input().split()))
validlist = []
for i in lista:
    if i > 0:
        validlist.append(i)

a = validlist[0]
b = validlist[1]

total = 0
for j in range(b):
    total += a
    a += 1
print(total)
