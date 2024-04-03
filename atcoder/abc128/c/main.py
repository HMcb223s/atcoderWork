n, m = map(int, input().split())

s = []
for i in range(m):
    k, *_ = map(int, input().split())
    for j in range(k):
        _[j] -= 1
    s.append(_)

p = list(map(int, input().split()))

ans = 0

for b in range (1 << n):
    ok = True
    for i in range(m):
        con = 0
        for v in s[i]:
            if b & (1 << v):
                con += 1
        if con % 2 != p[i]:
            ok = False
    if ok:
        ans += 1

print(ans)
