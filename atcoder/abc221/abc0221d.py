#!/usr/local/python
n = int(input())
a = []
b = []
for i in range(n):
  a_tmp, b_tmp = map(int, input().split())
  a.append(a_tmp)
  b.append(b_tmp)

x = [0 for _ in range(n)]

print(x)