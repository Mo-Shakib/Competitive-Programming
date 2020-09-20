t = int(input())
stones = input()
count = 0
a = 0
b = 1
first_chr = stones[a]
second_chr = stones[b]
for i in range(t):
    if first_chr == second_chr:
        count += 1
        a += 1
        b += 1
    if b >= t:
        break
print(count)
    