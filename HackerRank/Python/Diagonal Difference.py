def diagonalDifference(arr):
    # Write your code here
    d1 = sum([arr[x][x] for x in range(n)]) 
    d2 = sum([arr[x][n-1-x] for x in range (n)])
    print(abs(d1-d2))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    diagonalDifference(arr)
