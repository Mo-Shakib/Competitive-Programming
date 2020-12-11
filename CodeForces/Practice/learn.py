n = int(input())
factors = []
dict = {}
i = 2
while n >= 2:
    if n % i == 0:
        factors.append(i)
        n //= i
    else:
        i += 1
print(factors)


