n, k = map(int, input().split())
p = list(map(int, input().split()))
e = [0] * n

for i in range(n):
    e[i] = (1 + p[i]) / 2

total = 0
for i in range(k):
    total += e[i]

ans = total

for i in range(n-k):
    total += e[i+k] - e[i]
    # print(ans, total)

    if total > ans:
        ans = total

print(ans)
