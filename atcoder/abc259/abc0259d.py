#!/usr/local/python
n = int(input())
sx, sy, tx, ty = map(int, input().split())
x = [0] * n
y = [0] * n
r = [0] * n
for i in range(n):
  x[i], y[i], r[i] = map(int, input().split())

print("Yes")