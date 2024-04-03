#!/usr/local/python
n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

print(min(x), max(x), min(y), max(y))

# dis = (-x2)^2 + (y1-y2)^2

print(x)
print(y)