x = int(input())

a = (int(x/5))
left = x % 5
b = (int(left/4))
left = left % 4
c = (int(left/3))
left = left % 3
d = (int(left/2))
e = left % 2

print(a + b + c + d + e)

