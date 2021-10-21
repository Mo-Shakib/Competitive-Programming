umair = list(map(int, input().split()))
zuaina = list(map(int, input().split()))

if sum(umair) > sum(zuaina):
    print('umair wins the buffet')
else:
    print('zuaina wins the buffet')
