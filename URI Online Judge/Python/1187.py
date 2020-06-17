# Problem link: https://www.urionlinejudge.com.br/judge/en/problems/view/1187
op = input()
total = 0
count = 0
for row in range(12):
    for colum in range(12):
        value = float(input())
        if (colum > row) and ((row + colum) < 11):
            total += value
            count += 1
if op == 'S':
    print('{:.1f}'.format(total))
else:
    print('{:.1f}'.format(total/count))
