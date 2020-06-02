h1, m1, h2, m2 = map(int, input().split())

time1 = (h1 * 60) + m1
time2 = (h2 * 60) + m2

if time1 > time2:
    hr1 = (1440 - time1) + time2
    xh = int(hr1 / 60)
    xm = hr1 % 60
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(xh, xm))


elif time2 > time1:
    hr2 = time2 - time1
    yh = int(hr2 / 60)
    ym = hr2 % 60
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(yh, ym))


elif time1 == time2:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
