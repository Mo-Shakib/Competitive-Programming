for i in range(int(input())):
    nums = list(map(int, input().split()))
    for i in nums:
        if nums & 1 == 1:
            print('odd')
