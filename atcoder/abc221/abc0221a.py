#!/usr/local/python
a, b = map(int, input().split())

n = a - b 
ans = 1
for i in range(n):
  ans = ans * 32

print(ans)
