a, b = map(int, input().split())

if a > b:
    hr1 = (24 - a) + (-(0 - b))
    print("O JOGO DUROU {} HORA(S)".format(hr1))
elif b > a:
    hr2 = b - a
    print("O JOGO DUROU {} HORA(S)".format(hr2))
elif a == b:
    print("O JOGO DUROU 24 HORA(S)")