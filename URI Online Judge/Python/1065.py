lista = []
values = 0
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))

for i in lista:
    if (i % 2 == 0):
        values += 1
print("{} valores pares".format(values))