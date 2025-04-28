k, n = map(int, input().split())
a = list(map(int, input().split()))

a.append(a[0] + k)

max_distance = 0
for i in range(1, n + 1):
    max_distance = max(max_distance, a[i] - a[i - 1])
print(k - max_distance)
