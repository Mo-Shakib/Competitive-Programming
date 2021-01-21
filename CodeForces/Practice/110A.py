# https://codeforces.com/problemset/problem/110/A

def solution(x):
    lst = ['4','7']
    lst2 = []
    for i in x:
        if i not in lst:
            return "NO"
        else:
            lst2.append(i)
    if len(set(lst2)) > 1:
        return "YES"


number = input()
print(solution(number))

