lista = []
for i in range(0, 20):
    lista.append(int(input()))

listb = lista[::-1]
for j in range(0, 20):
    print('N[{}] = {}'.format(j, listb[j]))
