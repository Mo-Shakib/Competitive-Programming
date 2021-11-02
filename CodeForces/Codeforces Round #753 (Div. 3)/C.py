        
def solution(arr):
    if len(arr) < 3:
        return arr[0]
    while len(arr) < 3:
        arr = sorted(arr, reverse=True)
        x = arr.pop()
        for i in range(len(arr)):
            arr[i] = arr[i] - x
    return min(arr)

n = int(input())
for i in range(n):
    lenth = int(input())
    x = list(map(int, input().split()))
    print(solution(x))
