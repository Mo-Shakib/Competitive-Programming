import string

alpha = list(string.ascii_lowercase)
numb = list(range(97, 123, 1))

for i, j in zip(alpha, numb):
    print('{1} e {0}'.format(i, j))