string1 = input()
string2 = input()
string1 = string1.lower()
string2 = string2.lower()
str1 = []
str2 = []
for i in string1:
    str1.append(ord(i))
for j in string2:
    str2.append(ord(j))
str1 = sorted(str1)
str2 = sorted(str2)

s1 = ''
s2 = ''
for k in str1:
    s1 += str(k)
for l in str2:
    s2 += str(l)
if int(s1) < int(s2):
    print(-1)
elif int(s2) < int(s1):
    print(1)
else:
    print(0)