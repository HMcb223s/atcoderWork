from collections import Counter


n = int(input())
a = list(map(int, input().split()))
counts = Counter(a)

ans = 0
for k, v in counts.items():
    if k < v:
        ans += v - k
    if k > v:
        ans += v

print(ans)
