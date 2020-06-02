# Starting date:
dia, day1 = input().split()
day1 = int(day1)
h1, m1, s1 = input().split(":")

# Ending date:
dia, day2 = input().split()
day2 = int(day2)
h2, m2, s2 = input().split(":")

# Calculations:

start_time = int(day1) * 86400 + int(h1) *3600 + int(m1) *60 + int(s1)
end_time = int(day2) * 86400 + int(h2) *3600 + int(m2) *60 + int(s2)

total_time = abs(end_time - start_time)

# Output calculations:
day = int(total_time / 86400)
hour = int((total_time % 86400) / 3600)
minute = int((total_time % 3600) / 60)
second = int(total_time % 60)
# Output:
print(str(day) + " dia(s)")
print(str(hour) + " hora(s)")
print(str(minute) + " minuto(s)")
print(str(second) + " segundo(s)")
