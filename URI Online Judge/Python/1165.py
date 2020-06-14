test_case = int(input())
count = 0
while True:
    n = int(input())
    total_div = 0
    for i in range(1, n):
        if n % i == 0:
            total_div += i
    if total_div > 2:
        print('{} nao eh primo'.format(n))
    else:
        print('{} eh primo'.format(n))
    count += 1
    if count == test_case:
        break

