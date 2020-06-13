total_age = 0
count = 0
while True:
    n = int(input())
    if n >= 0:
        total_age += n
        count += 1
    else:
        break

print('{:.2f}'.format(total_age/count))
