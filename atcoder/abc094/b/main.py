n, m, x = map(int, input().split())
a = list(map(int, input().split()))

r_cost = 0
l_cost = 0

for i in range(x, n + 1):
    if i in a:
        r_cost += 1

for i in range(x, 0, -1):
    if i in a:
        l_cost += 1

print(min(r_cost, l_cost))
