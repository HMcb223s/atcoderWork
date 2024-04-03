a, b = map(int, input().split())

must = (b - 1) // (a - 1)
rem = (b - 1) % (a - 1)

if rem >= 1:
    print(must + 1)
else:
    print(must)