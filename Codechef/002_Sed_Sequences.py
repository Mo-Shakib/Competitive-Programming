# https://www.codechef.com/LTIME91B/problems/SEDARR

def findMinOpration(arr, k):
    if sum(arr) % k == 0:
        return 0
    return 1


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(findMinOpration(arr, k))
