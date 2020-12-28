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
            
a = [1,2,3,4,5]
x = 6
print(get_arr(a, x))