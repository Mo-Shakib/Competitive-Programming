colum = int(input())
op = input()

total = 0

for i in range(12):
    for j in range(12):
        value = float(input())
        if j == colum:
            total += value

if op == 'S':
    print('{:.1f}'.format(total))
else:
    print('{:.1f}'.format(total/12))
