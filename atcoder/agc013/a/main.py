n = int(input())
a = list(map(int, input().split()))

ans = 1
up = down = False
for i in range(n - 1):
    if a[i] < a[i+1]:
        up = True
    if a[i] > a[i+1]:
        down = True

    if up and down:
        ans += 1
        up = down = False

print(ans)
