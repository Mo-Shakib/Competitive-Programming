while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        start = n
    else:
        start = n + 1
    total = 0
    for i in range(start, start + 2 * 5, 2):
        total += i
        
    print(total)

