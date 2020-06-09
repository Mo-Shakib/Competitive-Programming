import math
import os
import random
import re
import sys

# Complete the solve function below.
meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())


tip_amount = meal_cost * tip_percent / 100
tax_amount = meal_cost * tax_percent / 100
total_cost = round(meal_cost + tip_amount + tax_amount)
print(total_cost)

