n, m = map(int, input().split())
x = list(map(int, input().split()))

if m <= n:
    print(0)
    exit(0)

x.sort(reverse=True)
# print(f'{x=}')
x_diff = [-1] * (m - 1) # x は m個の要素を持つので、m-1個の差分を持つ
for i in range(m - 1):
    x_diff[i] = x[i] - x[i + 1]
x_diff.sort(reverse=True)

print(sum(x_diff[(n-1):]))
