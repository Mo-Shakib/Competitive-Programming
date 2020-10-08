# https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen
t = int(input())
marks_sheet = []

for i in range(t):
    name = input()
    score = float(input())
    temp = name, score
    marks_sheet.append(temp)
print(temp)

