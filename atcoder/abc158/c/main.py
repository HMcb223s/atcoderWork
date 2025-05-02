a, b = map(int, input().split())

for x in range(1, 10 ** 4 + 1):
    a_x = int(x * 0.08)
    b_x = int(x * 0.1)
    if a_x == a and b_x == b:
        print(x)
        exit(0)

print(-1)
