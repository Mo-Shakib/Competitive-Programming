import math
while True:
    values = input().split()
    if values == ['0']: 
        break
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])

    total = (a * b) * 100 / c

    print('{}'.format(int(math.sqrt(total))))
