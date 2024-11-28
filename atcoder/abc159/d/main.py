def myfunc(x, y):
    return x * y // 2

n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (n + 1)
for v in a:
    cnt[v] += 1

total = 0
for i in range(1, n + 1):
    total += myfunc(cnt[i], cnt[i] - 1)

for v in a:
    ans = total - myfunc(cnt[v], cnt[v] - 1) + myfunc(cnt[v] - 1, cnt[v] - 2)
    print(ans)
