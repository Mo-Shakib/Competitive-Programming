# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/
for i in range(int(input())):
    seat_no = int(input())

    if (seat_no % 6 == 0) or ((seat_no - 1)%6 == 0) or ((seat_no + 5)%6 == 0):
        temp = 'WS'
    elif ((seat_no % 2 == 0) or ((seat_no - 3) % 2 == 0)) and (seat_no % 6 != 0):
        temp = 'MS'
    else:
        temp = 'AS'

    n = seat_no % 12 if seat_no % 12 else 12

    fsn = seat_no + (13 - 2*n)
    print(fsn, temp)