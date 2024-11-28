n = int(input())
s = [0] * n
not10_s = []
for _ in range(n):
    s[_] = int(input())

for v in s:
    if v % 10 != 0:
        not10_s.append(v)

ans = sum(s)
if ans % 10 == 0:
    if len(not10_s) == 0:
        ans = 0
    else:
        ans -= min(not10_s)
print(ans)
