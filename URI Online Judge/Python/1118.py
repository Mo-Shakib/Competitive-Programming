# URI Online Judge | 1118 - Several Scores with Validation
count = 'yes'
while count == 'yes':
    count2 = 0
    total_mark = 0
    while count2 < 2:
        mark = float(input())
        if 0 <= mark <= 10:
            total_mark += mark
            count2 += 1
        else:
            print('nota invalida')
    print('media = {:.2f}'.format(total_mark/2))
    print('novo calculo (1-sim 2-nao)')
    
    n = 0
    while True:
        n = int(input())
        if n == 1:
            count = 'yes'
            break
        elif n == 2:
            count = 'x'
            break
        else:
            print('novo calculo (1-sim 2-nao)')

