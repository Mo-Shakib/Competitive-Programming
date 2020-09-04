# https://www.urionlinejudge.com.br/judge/en/problems/view/1199
while True:
    n = input()
    if n == '-1':
        break
    if n.isdigit():
        n = hex(int(n))
        n = n[:2] + n[2:].upper()
    else:
        n = int(n, 16)
    print(n)