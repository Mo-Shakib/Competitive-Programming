# https://www.codechef.com/problems/HS08TEST

def Balance(x, balance):
    if (int(x) % 5 != 0) or (int(x) > (balance - 0.50)):
        return '{:.2f}'.format(balance)

    return '{:.2f}'.format(balance - (x + 0.50))

x, balance = map(float, input().split())
print(Balance(x, balance))
