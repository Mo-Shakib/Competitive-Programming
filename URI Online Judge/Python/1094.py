n = int(input())
total = c = r = s = 0

for i in range(0, n):
    a, b = input().split()
    a, b = [int(a), str(b)]

    total = total + a
    if b == 'C':
        c = c + a
    elif b == 'R':
        r = r + a
    if b == 'S':
        s = s + a

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))

print("Percentual de coelhos: {:.2f} %".format((c / total) * 100))
print("Percentual de ratos: {:.2f} %".format((r / total) * 100))
print("Percentual de sapos: {:.2f} %".format((s / total) * 100))
