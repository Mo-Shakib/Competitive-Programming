# https://www.urionlinejudge.com.br/judge/en/problems/view/1162
n = int(input())
while n > 0:
    n -= 1
    l = int(input())
    lt = input().split()

    swap = 0
    for i in range(l):
        for j in range(i + 1, l):
            if (int(lt[i]) > int(lt[j])):
                lt[i], lt[j] = lt[j], lt[i]
                swap += 1

    print('Optimal train swapping takes %d swaps.' % swap)