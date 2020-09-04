# https://www.urionlinejudge.com.br/judge/en/problems/view/1213
while True:
    try:
        n = input()
        l = 1
        c = 1
        while l % int(n) != 0:
            l = (10 * l + 1) % int(n)
            c += 1
        print(c)

    except EOFError:
        break