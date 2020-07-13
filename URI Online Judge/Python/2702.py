chiken, beef, pasta = map(int, input().split())
r_chiken, r_beef, r_pasta = map(int, input().split())
a = 0
b = 0
c = 0
if r_chiken > chiken:
    a += r_chiken - chiken
if r_beef > beef:
    b += r_beef - beef
if r_pasta > pasta:
    c += r_pasta - pasta

print(a+b+c)
