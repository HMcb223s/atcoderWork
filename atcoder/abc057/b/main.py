n, m = map(int, input().split())
a, b = [0] * n, [0] * n
c, d = [0] * m, [0] * m

for i in range(n):
    a[i], b[i] = map(int, input().split())
for j in range(m):
    c[j], d[j] = map(int, input().split())

for i in range(n):
    min_dist = 10**9
    ans = -1
    for j in range(m):
        dist = abs(a[i] - c[j]) + abs(b[i] - d[j])
        if dist < min_dist:
            min_dist = dist
            ans = j
    
    print(ans + 1)
