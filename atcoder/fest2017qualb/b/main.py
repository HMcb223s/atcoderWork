n = int(input())
d = sorted(list(map(int, input().split())))
m = int(input())
t = sorted(list(map(int, input().split())))

j = 0
for t_i in t:
    while j < n and d[j] < t_i:
        j += 1
    if j == n or d[j] > t_i:
        print("NO")
        exit(0)
    j += 1

print("YES")
