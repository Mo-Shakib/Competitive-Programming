# https://codeforces.com/problemset/problem/236/A
userName = input()
distinct = []
for i in userName:
    if i not in distinct:
        distinct.append(i)
if len(distinct) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')