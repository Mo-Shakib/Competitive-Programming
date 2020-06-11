#URI Online Judge | 1101 Sequência de Números e Soma
while True:
    x, y = map(int, input().split())
    if x <= 0 or y <= 0:
        break
    else:
        if x > y:
            maxv = x
            minv = y
        else:
            maxv = y
            minv = x

        total = 0
        for i in range(minv, maxv+1):
            total += i
            print(i, end=" ")
        print('Sum={}'.format(total))
            
        
