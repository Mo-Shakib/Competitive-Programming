import math
t = int(input())
for i in range(t):
    a = int(input())
    b = math.sqrt(a)
    c = a - (math.pi*(b/2)**2)
    d = (2*math.pi*(b/2))
    print(c,d)