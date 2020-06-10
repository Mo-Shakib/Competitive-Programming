test = int(input())
count = 0
while True:
    x, y = map(int, input().split())
    
    if y != 0:
        print("{:.1f}".format(x/y))
    elif y == 0:
        print('divisao impossivel')

    count += 1
    if count == test:
        break
