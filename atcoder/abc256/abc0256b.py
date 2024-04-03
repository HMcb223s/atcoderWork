#!/usr/local/python
n = int(input())
a = list(map(int, input().split()))

p = 0

l = [0, 0, 0, 0]
for i in range(n):
  l[0] = 1
  # print("l:", l)
  for _ in range(a[i]):
    p += l.pop()
    l.insert(0, 0)
    # print("p:", p)

print(p)