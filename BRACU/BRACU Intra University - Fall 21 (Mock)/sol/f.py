n = int(input())
boxs = list(map(int, input().split()))
sorted_boxs = sorted(boxs)
sorted_boxs_2 = set(sorted_boxs)
size = n - len(sorted_boxs_2) + 1
print(size)


# 1 1 2 2 2 3 3 4 5

# 1 2 3 4 5 # 1 2 3 # 2 -> 3


# 1 1 2 2 3 4
# 1 2 3 4 # 1 2
# 1 # 1
# 2, 3, 1, 1, 4 -> 1, 2, 3, 4
