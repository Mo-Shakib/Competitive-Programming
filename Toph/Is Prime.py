# https://toph.co/p/is-prime
number = int(input())
count = 0
for i in range(2, number):
    if number % i == 0:
        count += 1
if count < 1:
    print('Yes')
else:
    print('No')