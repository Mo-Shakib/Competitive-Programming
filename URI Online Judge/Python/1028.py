def euclides_mdc(dividendo, divisor):
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp    
    return dividendo
qtd = int(input())
cont = 0
while cont < qtd:
    numeros = input().split()
    n1 = int(numeros[0])
    n2 = int(numeros[1])
    print (euclides_mdc(n1, n2))
    cont += 1