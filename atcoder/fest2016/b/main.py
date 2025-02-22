n = int(input())
a = list(map(int, input().split()))
a = [x-1 for x in a]
cnt = 0
for i in range(n):
    if i == a[a[i]]:
        cnt += 1

print(cnt // 2)
