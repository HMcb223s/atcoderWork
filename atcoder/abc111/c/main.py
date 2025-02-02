from collections import Counter
n = int(input())
v = list(map(int, input().split()))

v1 = Counter(v[::2])
v2 = Counter(v[1::2])

c1, c2=[], []
for x, cnt in v1.items():
    c1.append((cnt, x))
for x, cnt in v2.items():
    c2.append((cnt, x))

c1.sort(reverse=True)
c2.sort(reverse=True)

# print(f'{c1=} {c2=}')
if c1[0][1] != c2[0][1]:
    print(n - (c1[0][0] + c2[0][0]))
    exit(0)

x = 0
if len(c1) >= 2:
    x = max(x, c1[1][0])
if len(c2) >= 2:
    x = max(x, c2[1][0])

print(n - (c1[0][0] + x))
