# Make fibonacci series
a = 0
b = 1
fibo = [0, 1]
count = 0
while count < 60:
    c = a + b
    a = b
    b = c
    fibo.append(c)
    count += 1
# After making fibonacci series
count2 = 0
t = int(input())
while True:
    n = int(input())
    print('Fib({}) = {}'.format(n, fibo[n]))
    count2 += 1
    if count2 == t:
        break
