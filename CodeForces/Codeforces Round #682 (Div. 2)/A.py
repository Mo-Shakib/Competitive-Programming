a = [x//x for x in range(201) if x%2 == 1]

t = int(input())
for i in range(t):
    n = int(input())
    out = a[:n]
    output = ' '.join(map(str, out))
    print(output)



