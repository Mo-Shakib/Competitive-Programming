# https://vjudge.net/contest/472762#problem/C

def solution(arr):
    arr = sorted(arr)
    result = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] & arr[j] >= arr[i] ^ arr[j]:
                result += 1                
    print(result)

n = int(input())
for i in range(n):
    a = int(input())
    x = list(map(int, input().split()))
    solution(x)
