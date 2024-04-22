n = int(input())
a = [0] + list(map(int, input().split()))

b = [0] * (n + 1)
for i, a_i in enumerate(a):
    b[a_i] = i

ans = []
a_sorted = [_ for _ in range(n + 1)]

for i in range(1, n + 1):
    if a[i] != a_sorted[i]:
        a_i, b_i = a[i], b[i]
        ans.append([i, b_i])
        a[i], a[b_i] = a[b_i], a[i]
        b[a[b_i]] = b_i

print(len(ans))

if ans:
    for x in ans:
        print(*x)
