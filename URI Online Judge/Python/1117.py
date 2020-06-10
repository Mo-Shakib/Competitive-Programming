count = 0
total_marks = 0
while count < 2:
    marks = float(input())
    if (0 <= marks <= 10):
        total_marks += marks
        count += 1
    else:
        print('nota invalida')

print('media = {:.2f}'.format(total_marks/2))

    