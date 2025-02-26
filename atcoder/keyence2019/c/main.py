n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
ans = 0
y = []
for i in range(n):
    if a[i] < b[i]:
        s += b[i] - a[i]
        ans += 1
    else:
        y.append(a[i] - b[i])

# print(f'{a=} {b=} {y=} {s=}')
y.sort()
tmp = 0
while s > 0 and y:
    # print(f'{ans=} {tmp=} {y=} {s=}')
    tmp = y.pop()
    ans += 1
    s -= tmp

if s > 0:
    print(-1)
else:
    print(ans)

