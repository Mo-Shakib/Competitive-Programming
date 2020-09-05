lista = input().split()
a = float(lista[0])
b = float(lista[1])
print(str("%.2f"%(((b - a)/a)*100))+"%")