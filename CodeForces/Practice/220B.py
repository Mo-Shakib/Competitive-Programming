# https://codeforces.com/problemset/problem/230/B

c = int(input())
p_ints = list(map(int, input().split()))
for n in p_ints:
    factors = []
    dict = {}
    i = 2
    while n >= 2:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    for i in factors:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    total_divisor = 1
    for values in dict.values():
        total_divisor *= (values+1)
        
    # print(total_divisor)
    if total_divisor == 3:
        print('YES')
    else:
        print('NO')
