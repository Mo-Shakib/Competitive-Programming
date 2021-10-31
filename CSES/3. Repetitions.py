# https://cses.fi/problemset/task/1069

def solution(strin):
    longest = 0
    arr = [0]
    lst = strin[0]
    for i in strin:
        if i == lst:
            longest += 1
        else:
            lst = i
            arr.append(longest)
            longest = 1
    arr.append(longest)
    return max(arr)

print(solution(input()))