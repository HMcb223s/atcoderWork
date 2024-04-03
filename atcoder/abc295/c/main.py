from collections import Counter

n = int(input())
a = list(map(int, input().split()))
cnt_a = Counter(a)
ans = 0
# print(cnt_a)
for k, v in cnt_a.items():
    ans += v // 2

print(ans)