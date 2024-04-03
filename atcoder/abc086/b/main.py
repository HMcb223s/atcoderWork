import math
x = int("".join(input().split()))

if math.sqrt(x).is_integer():
    print("Yes")
else:
    print("No")