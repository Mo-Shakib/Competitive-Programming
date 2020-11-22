# https://codeforces.com/contest/266/problem/A
t = input()
count = 0
stones = input()
if len(stones) == 1:
        print(0)
else:
    for i in range(1,len(stones)):
        if stones[i] == stones[i-1]:
            count += 1
        
    print(count)

# accepted xD