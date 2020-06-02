import math

value1 = input().split()
value2 = input().split()

x1 = float(value1[0])
y1 = float(value1[1])
x2 = float(value2[0])
y2 = float(value2[1])

result = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
# math.hypot() can be use here

print("%.4f"%result)
