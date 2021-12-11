# https://vjudge.net/contest/472762?fbclid=IwAR33bcT3Du8Y9V6YOtSbY-ULpZuUis3fWp4VjYUI3H_zx52G9iEoaax-tas#problem/B

def remove_subsequences(x):
    total_cost = 0
    for i in range(1, len(x)):
        total_cost += x[i] | x[i-1]
    return total_cost

n = int(input())
for i in range(n):
    lenth = int(input())
    x = list(map(int, input().split()))
    print(remove_subsequences(x))    