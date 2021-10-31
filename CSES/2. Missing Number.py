# https://cses.fi/problemset/task/1083

n = int(input())
numbers = list(map(int, input().split()))

all_numbers = [x for x in range(1, n+1)]

missing = set(all_numbers) - set(numbers)

print(' '.join(str(i) for i in missing))