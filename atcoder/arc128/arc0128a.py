#!/usr/local/python
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

n = I()
a = LI()
v = [0 for _ in range(n)]

# a.insert(0, 1) # a[] has n+1 int
# for i in range(n-1):
#   if a[i] < a[i+1] and a[i+1] >= a[i+2]:
#       v[i] = 1
#       v[i+1] = 1
#       i = i + 1
for i in range(n-1):
  if a[i] < a[i+1] and a[i+1] >= a[i+2]:
      v[i] = 1
      v[i+1] = 1
      i = i + 1

print(' '.join(map(str, v)))