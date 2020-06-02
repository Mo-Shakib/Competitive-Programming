# Take inpute
hour = int(input())
speed = int(input())
# Calculation
distance = hour * speed
fuel = distance / 12
# output
print("%.3f" %fuel)