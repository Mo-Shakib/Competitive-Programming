# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/

for i in range(int(input())):
    g, p = map(int, input().split())
    gl = 0
    pl = 0
    for j in range(int(input())):
        a, b = map(int, input().split())
        if a == 1:
            gl += 1
        if b == 1:
            pl += 1
    type1 = (g*gl) + (p*pl)
    type2 = (g*pl) + (p*gl)
    print(min(type1, type2))

