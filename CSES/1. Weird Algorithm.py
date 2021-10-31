# https://cses.fi/problemset/task/1068

output = []
n = int(input())
output.append(n)

while n != 1:
    if n % 2 == 0:
        n //= 2
        output.append(n)
    else:
        n = n * 3 + 1
        output.append(n)
        
print(' '.join(str(x) for x in output))