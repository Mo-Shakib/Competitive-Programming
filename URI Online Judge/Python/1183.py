op = input()
total = 0
count = 0
for row in range(12):
    for colum in range(12):
        value = float(input())
        if (colum > row):
            total += value
            count += 1
if op == 'S':
    print('{:.1f}'.format(total))
else:
    print('{:.1f}'.format(total/count))
