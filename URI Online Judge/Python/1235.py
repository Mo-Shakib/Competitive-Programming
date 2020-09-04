# https://www.urionlinejudge.com.br/judge/en/problems/view/1235
n = int(input())

while(n > 0):
    n -= 1
    c = input()
    m = int(len(c)/2) -1
    out = c[m::-1] + c[len(c)-1:m:-1]
    print(out)