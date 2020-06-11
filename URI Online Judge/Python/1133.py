a = int(input())
b = int(input())

if a > b:
    maxv = a
    minv = b
else:
    maxv = b
    minv = a

total = 0
for i in range(minv+1, maxv):
    if (i % 5 == 2) or (i % 5 == 3):

        print(i)
