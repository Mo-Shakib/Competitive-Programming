# https://www.codechef.com/problems/VACCINE1

from math import ceil

def vaccine(d1, v1, d2, v2, p):
    total = 0
    days = 1
    min_day = min(d1, d2)
    max_day = max(d1, d2)

    if min_day == d1:
        production = v1
    else:
        production = v2

    if d1 == d2:
        return ceil(p / (v1 + v2))

    while total < p:
        if max_day != min_day:
            min_day += 1
            total += production
        elif min_day == max_day:
            total += (v1 + v2)
        days += 1
    return days


d1, v1, d2, v2, p = map(int, input().split())
print(vaccine(d1, v1, d2, v2, p))
