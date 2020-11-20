# https://www.hackerrank.com/challenges/nested-list/problem
from decimal import Decimal
t = int(input())
marks = {}
for i in range(t):
    name = input()
    mark = input()

    if mark in marks:
        marks[mark] += [name]
    else:
        marks[mark] = [name]
    
a = []
for j in marks.keys():
    a.append(Decimal(j))

minv = min(a)

print(minv)
print(marks)
print(a)
# print(marks[minv])