#https://atcoder.jp/contests/abc179/tasks/abc179_a
user_input = input()
if user_input[-1] == 's':
    user_input += 'es'
else:
    user_input += 's'
print(user_input)