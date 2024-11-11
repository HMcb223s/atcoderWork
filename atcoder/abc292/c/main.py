n = int(input())
ans = 0
for i in range(1, n+1):
    ab, cd = i, n - i
    x, y = 0, 0

    for j in range(1, int(ab ** 0.5) + 1):
        if ab % j == 0:
            x += 1
            if ab != j*j:
                x += 1
    for j in range(1, int(cd ** 0.5) + 1):
        if cd % j == 0:
            y += 1
            if cd != j*j:
                y += 1
    # print(x, y)
    ans += x * y
print(ans)
