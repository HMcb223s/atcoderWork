n = int(input())
a = list(map(int, input().split()))
x = [-1] * n
for i, v in enumerate(a):
    x[v - 1] = i + 1

print(*x)