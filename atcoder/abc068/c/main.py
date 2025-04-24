n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    # 0-indexed
    a, b = [int(x) - 1 for x in input().split()]
    g[b].append(a)

# print(f'{g=}')
for i in g[-1]:
    for next in g[i]:
        if next == 0:
            print("POSSIBLE")
            exit()
print("IMPOSSIBLE")
