lista = []
values = 0
total = 0
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))

for i in lista:
    if (i > 0):
        values += 1
for i in lista:
    if (i > 0):
        total = total + i
print("{} valores positivos".format(values))
print('%.1f'%(total/values))