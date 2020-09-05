# https://www.urionlinejudge.com.br/judge/en/problems/view/2175
linha = input().split()
otavio = float(linha[0])
bruno = float(linha[1])
ian = float(linha[2])

if otavio < bruno and otavio < ian:
    print("Otavio")
elif bruno < otavio and bruno < ian:
    print("Bruno")
elif ian < otavio and ian < bruno:
    print("Ian")
else:
    print("Empate")