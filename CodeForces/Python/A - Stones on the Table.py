t = int(input())
stons = input()
r = 0
g = 0
b = 0
temp = stons[0]
count = 0
for i in range(t):
    if stons[count] == stons[count+1]:
        if stons[i] == 'R':
            r += 1
        elif stons[i] == 'B':
            b += 1
        elif stons[i] == 'G':
            g += 1
    count += 1
print(r+g+b)