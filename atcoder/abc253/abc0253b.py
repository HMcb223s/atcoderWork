#!/usr/local/python
h, m = map(int, input().split())

s = [input() for _ in range(h)]

count = 0

for i in range(h):
  for j in range(m):
    if s[i][j] == 'o':
      if count == 0:
        a, b = i, j
        count += 1
      elif count == 1:
        c, d = i, j
      
#    print(s[i][j])

#print(a, b, c, d)
print(abs(c-a) + abs(d-b))