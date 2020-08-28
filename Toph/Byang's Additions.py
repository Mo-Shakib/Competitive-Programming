# https://toph.co/p/byang-learns-to-add-almost
a, b = input().split()
count = 0
for i in range(len(-1, a)):
    if int(a[i]) + int(b[i]) >= 10:
        count += 1
if count < 1:
    print('No')
else:
    print('Yes')