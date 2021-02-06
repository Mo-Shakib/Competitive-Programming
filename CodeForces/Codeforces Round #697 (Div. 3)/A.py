import math
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def check_odd(number):
    for i in number:
        if (i > 1) and i % 2 == 1:
            return 'YES'
            
    return 'NO'


t = int(input())
for a in range(t):
    num = int(input())
    x = list(divisorGenerator(num))
    print(check_odd(x))

    