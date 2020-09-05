# https://www.urionlinejudge.com.br/judge/en/problems/view/2176
linha = input()
qtd = 0
for i in linha:
    if int(i) == 1:
        qtd += 1
if qtd %2 != 0 and qtd != 0:
    linha += str(1)
else:
    linha += str(0)
print(linha)