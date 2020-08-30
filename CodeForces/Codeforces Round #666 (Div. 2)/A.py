# https://codeforces.com/contest/1397/problem/0
t = int(input())
for i in range(t):
    t_2 = int(input())
    total_string = ''
    dicts = {}
    for j in range(t_2):
        string = input()
        total_string += string
    for k in total_string:
        if k in dicts:
            dicts[k] += 1
        else:
            dicts[k] = 1
    total = 0
    for l in dicts.values():
        total += l
    temp = 0
    for m in dicts.values():
        if total % m == 0:
            pass
        else:
            temp += 1
    if temp == 0:
        print('YES')
    else:
        print('NO')
    