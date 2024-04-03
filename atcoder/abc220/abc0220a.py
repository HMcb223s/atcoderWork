#!/usr/local/python
a, b, c = map(int, input().split())

ans = -1
for i in range(5):
  if c * i >= a and c * i <= b:
    ans = c * i

print(ans)