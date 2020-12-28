def get_arr(arr, n):
    if (len(arr) == 1) and (sum(arr) != n):
        return 'No'
    if (sum(arr) == n):
        return 'Yes'
    while True:
        arr = sorted(arr)
        mid = int((max(arr)+min(arr))/2)  # mid
        left_arr = list(filter(lambda x: x <= mid, arr))  # left array
        right_arr = list(filter(lambda x: x > mid, arr))  # right array

        if mid <= n:
            arr = left_arr
        else:
            arr = right_arr

        if sum(arr) == n:
            return 'Yes'
            

        if (len(arr) == 1) and n == sum(arr):
            return 'Yes'
            

        if (len(arr) == 1) and n != sum(arr):
            return 'No'


t = int(input())  # test cases
for i in range(t):
    n, q = map(int, input().split())
    arrey = list(map(int, input().split()))  # arr input

    for i in range(q):
        x = int(input())  # sum input
        print(get_arr(arrey, x))
