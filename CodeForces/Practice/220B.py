# https://codeforces.com/problemset/problem/230/B
c = int(input())
p_ints = list(map(int, input().split()))
for j in p_ints:
    count = 0
    x = [j for j in range(1, j+1)]
    for i in x:
        if j % i == 0:
            count += 1

    if count == 3:
        print('YES')
    else:
        print('NO')

# Time limit exceeded on test 5