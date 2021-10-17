# https://codeforces.com/contest/1593/problem/B

def main(n):
    lenth = len(n)
    ans = []
    for i in range(lenth):
        for j in range(i, lenth):
            if (int(n[i])*10 + int(n[j])) % 25 == 0:
                a = int(n[:j+1])
                res = abs(len(n) - len(str(a)))
                ans.append(res)

    print(f'{min(ans)}')

for i in range(int(input())):
    main(input())