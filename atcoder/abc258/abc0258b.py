#!/usr/local/python
import math
n = int(input())
# a = [list(map(int, input().split())) for l in range(n)]

if n <= 1:
  print(int(input()))
  exit(0)

a = []
for _ in range(n):
    array = list(input())
    a.append(array)


# print(a)
ans = 0

for r in range(8):
  for i in range(n):
    for j in range(n):

      tmp = []
      for k in range(n):
        if r == 0:
          tmp.append(a[(i+k)%n][j])
        elif r == 1:
          tmp.append(a[(i+k)%n][(j+k)%n])
        elif r == 2:
          tmp.append(a[i][(j+k)%n])
        elif r == 3:
          tmp.append(a[(i-k)%n][(j+k)%n])
        elif r == 4:
          tmp.append(a[(i-k)%n][j])
        elif r == 5:
          tmp.append(a[(i-k)%n][(j-k)%n])
        elif r == 6:
          tmp.append(a[i][(j-k)%n])
        elif r == 7:
          tmp.append(a[(i+k)%n][(j-k)%n])
        
      x = int("".join(tmp))
      ans = max(ans, x)
print(ans)