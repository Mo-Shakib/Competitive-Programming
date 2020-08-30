t = int(input())
stones = input()
count = 0
for i in range(t):
    if stones[i] == stones[i-1]:
        count += 1
if count == t:
    print(count - 1)
else:
    print(count)
    