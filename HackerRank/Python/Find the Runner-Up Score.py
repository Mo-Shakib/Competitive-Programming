# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen

t = int(input())
x_list = list(map(int, input().split()))
maxvalue = max(x_list)
new_list = []
for i in x_list:
    if i != maxvalue:
        new_list.append(i)
print(max(new_list))
