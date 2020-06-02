# Time Conversion

time = int(input())
hr = int(time / 3600)
left_time = time % 3600
min = int(left_time / 60)
sec = int(left_time % 60)
print("{}:{}:{}".format(hr, min, sec))