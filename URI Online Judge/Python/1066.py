lista = []

lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))

even = 0
odd = 0
pos = 0
neg = 0

for i in lista:
    if (i % 2 == 0):
        even += 1
for i in lista:
    if (i % 2 == 1):
        odd += 1
for i in lista:
    if (i > 0):
        pos += 1
for i in lista:
    if (i < 0):
        neg += 1

print("{} valor(es) par(es)".format(even))
print("{} valor(es) impar(es)".format(odd))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))

