wet = int(int(input()))
if 1 <= wet <= 100:
    if (wet % 2 == 0) and wet > 2:
        print("YES")
    else:
        print("No")