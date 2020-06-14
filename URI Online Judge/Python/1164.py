test_number = int(input())
count = 0
while True:
    n = int(input())
    div_total = 0
    for i in range(1, n, 1):
        if n % i == 0:
            div_total += i
    
    if div_total == n:
        print('{} eh perfeito'.format(n))
    else:
        print('{} nao eh perfeito'.format(n))
    
    count += 1
    if count == test_number:
        break