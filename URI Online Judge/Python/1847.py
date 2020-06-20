#Problem link: https://www.urionlinejudge.com.br/judge/en/problems/view/1847

a, b, c = map(int, input().split())
if a > b and b <= c:
    print(':)')
    #2
if a < b and b >= c:
    print(':(')
    #3
if a < b and b < c and (b - a) > (c - b):
    print(':(')
    #4
if a < b and b < c and (b - a) <= (c - b):
    print(':)')
    #5
if a > b and b > c and (a - b) > (b - c):
    print(':)')
    #6
if a > b and b > c and (a - b) <= (b - c):
    print(':(')
    #7
if a == b and b < c:
    print(':)')
    #8
if a == b and b > c:
    print(':(')

    #pegadinha
if a == b and b == c:
    print(':(')
