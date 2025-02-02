n, yen = map(int, input().split())

for i in range(n + 1):
    for j in range(n + 1):
        k = n - (i + j)

        if 0 <= k:
            if 10_000 * i + 5_000 * j + 1_000 * k == yen:
                print(i, j, k)
                exit(0)

print(-1, -1, -1)
