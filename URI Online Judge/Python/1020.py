# Age in days
age_in_days = int(input())

year = int(age_in_days / 365)
day_left = age_in_days % 365
month = int(day_left / 30)
day_left = day_left % 30
print(str(year) + ' ano(s)')
print(str(month) + ' mes(es)')
print(str(day_left) + ' dia(s)')
