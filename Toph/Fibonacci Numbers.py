# https://toph.co/p/fibonacci-numbers
a = 0
b = 1
sum = 0
count = 0
fib_list = []
while count < 53:
    fib_list.append(a)
    a = b
    b = sum
    sum = a + b
    count += 1
new = fib_list[3:]
n = int(input())
print(new[n-1])
