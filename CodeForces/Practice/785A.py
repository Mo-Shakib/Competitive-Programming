# https://codeforces.com/problemset/problem/785/A
stone = {'Tetrahedron':4, 'Cube':6,'Octahedron':8,'Dodecahedron':12,'Icosahedron':20}
total = 0
for i in range(int(input())):
    n = input()
    total += stone[n]

print(total)

# accepted