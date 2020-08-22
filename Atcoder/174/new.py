import math
t = int(input())
if t % 2 == 0:  t += 2
else:   t -= 2
print(t)
l = []
for i in range(t):
    num = float(input())
    if (-100 <= num <= 0):  l.append(math.floor(num))
    elif ( 0 <= num <= 100):    l.append(math.ceil(num))
    else:   l.append(num)
print(l)

