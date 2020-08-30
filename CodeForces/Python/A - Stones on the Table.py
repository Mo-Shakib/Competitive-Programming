t = int(input())
stons = input()
r = 0
g = 0
b = 0
for i in range(t):
    if stons[i-1] == stons[i]:
        if stons[i] == 'R':
            r += 1
        elif stons[i] == 'B':
            b += 1
        elif stons[i] == 'G':
            g += 1
print(r+g+b)