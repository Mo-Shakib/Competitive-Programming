# https://codeforces.com/contest/1397/problem/0
t = int(input())
for i in range(t):
    t_2 = int(input())
    total_string = ''
    for j in range(t):
        string = input()
        total_string += string
    if len(total_string) % t_2 == 0:
        print('YES')
    else:
        print('NO')