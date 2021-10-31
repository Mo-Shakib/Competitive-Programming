# target=int(input("Enter a Nth Number:"))

# 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323 ......

palindrom = []

# for i in range(10):
#     palindrom.append(i)

n = 101
x = 1
y = 0
s = 101
while n < 5000:
    if x % 10 == 0:
        y += 1
        n = s + (x * 10) + y
    palindrom.append(n)
    print(palindrom)
    print('x =', x)
    print('n = ',n)
    n += 10
    x += 1
    